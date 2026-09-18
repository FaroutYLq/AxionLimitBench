#!/usr/bin/env python3
"""AxionLimitBench baseline: a generic tool-using agent, one headless Claude Code
session per paper.

The "system" here is deliberately minimal: the model, seven Claude Code built-in
tools (Read / Write / Edit / Bash / Glob / Grep / WebFetch, verified via the CLI's
init event), and the public
task card (docs/TASK.md) appended to the system prompt. There is no domain
harness: no convention registry, no gates, no channel routing, no consensus.
The agent may read the PDF, fetch the paper's own arXiv e-print, and run any
code it likes inside a throwaway working directory; it must write
``result.json`` in the prediction schema (schema/prediction.schema.json).

Transport / billing
-------------------
``--transport auto`` starts on the Claude Code subscription (keychain OAuth)
and switches to API-key billing the moment the subscription window is
exhausted (never waits for the reset). The key is read from ``--api-key-file``
(default ``~/.aal_bench/axionlimitbench_api_key``), ``AXLB_API_KEY``, or the
parent shell's ``ANTHROPIC_API_KEY``; if none exists when the window closes,
the driver blocks and polls for the file every 60 s, printing a loud message. Every snapshot records the transport
that produced it.

Resume
------
Re-running with the same ``--outdir`` skips papers whose snapshot is present
and not an error stub. Timeouts and abstentions are kept (they are the
system's answer), errors are retried.

Audit
-----
The full stream-json transcript of every session is kept as
``<id>.events.jsonl`` next to the snapshot, and scanned for forbidden sources
(secondary compilations such as AxionLimits itself). A hit sets
``meta.leak_suspect`` so the scorer can exclude the paper.
"""
from __future__ import annotations

import argparse
import atexit
import hashlib
import json
import os
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DRIVER_VERSION = "0.1.4"
TASK_CARD_PATH = ROOT / "docs" / "TASK.md"
DEFAULT_IDS = ROOT / "data" / "measured_pool_ids.json"
DEFAULT_KEY_FILE = Path.home() / ".aal_bench" / "axionlimitbench_api_key"

# Parent-session variables that would silently change billing or confuse the
# child (the driver is normally launched from inside a Claude Code session).
SCRUB_ENV = (
    "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_BASE_URL",
    "ANTHROPIC_MODEL", "ANTHROPIC_SMALL_FAST_MODEL",
    "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX", "CLAUDECODE",
)
SCRUB_PREFIXES = ("CLAUDE_CODE_",)

USAGE_LIMIT_MARKERS = (
    "usage limit reached", "usage limit", "5-hour limit", "weekly limit",
    "reset at", "session limit", "hit your limit", "· resets", "limit resets",
    # 2026-09-15 23:15 incident: "You've hit your monthly spend limit · raise it
    # at claude.ai/settings/usage" matched none of the above, so ~210 papers
    # were stubbed as per-paper errors in 30 s instead of failing over.
    "spend limit", "monthly limit", "hit your", "claude.ai/settings/usage",
    "raise it at",
)
FATAL_MARKERS = (
    "credit balance", "billing", "invalid api key", "invalid x-api-key",
    "not logged in", "/login", "authentication",
)
RATE_MARKERS = (
    "rate limit", "too many requests", "429", "overloaded", "529",
    "service unavailable",
)
# Forbidden secondary sources: any hit in the transcript flags the paper.
LEAK_PATTERNS = (
    "cajohare", "axionlimits", "limit_data", "raw.githubusercontent.com",
    "github.com", "cajohare.github.io", "hepdata", "hepdata.net", "inspirehep",
    "inspirehep.net", "pdg.lbl.gov", "darkcast", "ciaran", "o'hare",
)
LEAK_HOST_PATTERNS = tuple(p for p in LEAK_PATTERNS if "." in p)
NETWORK_INDICATORS = ("http://", "https://", "curl ", "wget ", "git clone", "urlopen", "requests.get", "fetch(")
# Tool permission deny-list handed to the CLI (belt and braces over the task
# card's instructions and the transcript audit).
SETTINGS = {
    "permissions": {
        "deny": [
            "WebSearch",
            "WebFetch(domain:github.com)",
            "WebFetch(domain:raw.githubusercontent.com)",
            "WebFetch(domain:cajohare.github.io)",
            "WebFetch(domain:hepdata.net)",
            "WebFetch(domain:inspirehep.net)",
            "Bash(git clone:*)",
        ]
    }
}
# Explicit allow-list: the CLI's "default" set also exposes cron, worktree,
# messaging and task tools that a benchmark agent must never have.
ALLOWED_TOOLS = "Read,Write,Edit,Bash,Glob,Grep,WebFetch"

SNAPSHOT_FIELDS = (
    "paper_title", "coupling_type", "is_new_limit", "is_projection",
    "data_points", "data_source", "dm_density_assumed", "confidence_level",
    "extraction_confidence", "suggested_experiment_name",
    "coupling_convention", "notes",
)


class FatalRunError(RuntimeError):
    """An availability error: a property of the run, never of the paper."""


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def safe_id(aid: str) -> str:
    return aid.replace("/", "_")


def _read_key_file(path: Path) -> str:
    try:
        return path.read_text()
    except OSError:
        return ""


class Transport:
    """Current billing path, shared by all workers; flips cli -> api once."""

    def __init__(self, mode: str, key_file: Path):
        self.mode = mode
        self.key_file = key_file
        self.lock = threading.Lock()
        self.switched_at: float | None = None

    def api_key(self) -> str | None:
        """Failover key, in order: AXLB_API_KEY, the key file, or the parent
        shell's ANTHROPIC_API_KEY (scrubbed from the child during the
        subscription phase, but a legitimate credit source once the window
        closes). The value is only ever passed through to the child env."""
        for src in (os.environ.get("AXLB_API_KEY", ""), _read_key_file(self.key_file),
                    os.environ.get("ANTHROPIC_API_KEY", "")):
            if src and src.strip():
                return src.strip()
        return None

    def child_env(self) -> dict:
        env = dict(os.environ)
        for k in list(env):
            if k in SCRUB_ENV or any(k.startswith(p) for p in SCRUB_PREFIXES):
                env.pop(k, None)
        env["CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"] = "1"
        with self.lock:
            mode = self.mode
        if mode == "api":
            key = self.api_key()
            if not key:
                raise FatalRunError("transport=api but no API key available")
            env["ANTHROPIC_API_KEY"] = key
        return env

    def on_usage_limit(self, text: str) -> None:
        """Subscription window exhausted: switch to API billing immediately."""
        with self.lock:
            if self.mode == "api":
                # API-side "usage limit" is a rate limit, not a window; the
                # caller backs off.
                return
            log(f"SUBSCRIPTION WINDOW EXHAUSTED: {text[:160]!r}")
            while self.api_key() is None:
                log(f"waiting for API key at {self.key_file} (or AXLB_API_KEY); "
                    "polling every 60 s -- the run is PAUSED, not failed")
                time.sleep(60)
            self.mode = "api"
            self.switched_at = time.time()
            log("SWITCHED transport: cli (subscription) -> api (credit)")


def classify_error_text(text: str) -> str:
    low = (text or "").lower()
    if any(m in low for m in USAGE_LIMIT_MARKERS):
        return "usage_limit"
    if any(m in low for m in FATAL_MARKERS):
        return "fatal"
    if any(m in low for m in RATE_MARKERS):
        return "rate"
    return "paper"


def build_argv(args, task_card: str) -> list[str]:
    argv = [
        args.claude_bin, "-p",
        "--model", args.model,
        "--output-format", "stream-json", "--verbose",
        "--no-session-persistence",
        "--setting-sources", "",
        "--strict-mcp-config",
        "--settings", json.dumps(SETTINGS),
        "--tools", ALLOWED_TOOLS,
        "--dangerously-skip-permissions",
        "--append-system-prompt", task_card,
    ]
    if args.max_budget_usd is not None:
        argv += ["--max-budget-usd", str(args.max_budget_usd)]
    if args.effort:
        argv += ["--effort", args.effort]
    return argv


def user_prompt(aid: str, work: Path) -> str:
    return (
        f"AxionLimitBench task for arXiv:{aid}.\n\n"
        f"The paper's PDF is at ./paper.pdf in the current working directory "
        f"({work}). Follow the AxionLimitBench task card in your system prompt. "
        f"Work only from this paper and its own arXiv e-print. When you are "
        f"done, write the prediction schema JSON to exactly this absolute path: "
        f"{work / 'result.json'} (not a relative path: your shell's working "
        f"directory persists between commands) and reply with the single line DONE."
    )


def parse_events(stdout: str) -> tuple[list[dict], dict | None]:
    events: list[dict] = []
    result = None
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        events.append(ev)
        if ev.get("type") == "result":
            result = ev
    return events, result


def scan_leaks(events_text: str) -> list[str]:
    """Forbidden-source patterns in what the AGENT ISSUED (tool_use inputs:
    commands, URLs, file paths) and in its own prose. Tool results are not
    scanned: paper text routinely cites github.com or INSPIRE, and reading
    the paper is the task. A hit means the agent tried to reach such a
    source, not that the paper mentioned one."""
    hits: set[str] = set()
    for line in events_text.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") != "assistant":
            continue
        for b in (ev.get("message") or {}).get("content") or []:
            if b.get("type") == "tool_use":
                # actions: host patterns always count; bare words (axionlimits,
                # cajohare, ...) only when the same call reaches the network,
                # because e-prints legitimately contain files with such names
                # (SNO's own figure is literally "AxionLimitsv2.pdf").
                blob = json.dumps(b.get("input")).lower()
                networked = (b.get("name") == "WebFetch"
                             or any(k in blob for k in NETWORK_INDICATORS))
                hits.update(p for p in (LEAK_PATTERNS if networked else LEAK_HOST_PATTERNS) if p in blob)
            elif b.get("type") == "text":
                # prose: the task card itself names AxionLimits, so only
                # host-like strings count here
                blob = str(b.get("text")).lower()
                hits.update(p for p in LEAK_HOST_PATTERNS if p in blob)
    return sorted(hits)


def normalise_result(raw: dict) -> tuple[dict, list[str]]:
    """Coerce the agent's result.json into the snapshot schema; never raises."""
    problems: list[str] = []
    out: dict = {}
    for k in SNAPSHOT_FIELDS:
        out[k] = raw.get(k)
    pts = []
    for p in raw.get("data_points") or []:
        try:
            if isinstance(p, dict):
                m, g = float(p.get("mass_eV", p.get("mass"))), float(p.get("coupling"))
            else:
                m, g = float(p[0]), float(p[1])
        except (TypeError, ValueError, IndexError, KeyError):
            problems.append(f"bad point {p!r}")
            continue
        if not (m > 0 and g > 0) or m != m or g != g:
            problems.append(f"non-positive/nan point {p!r}")
            continue
        pts.append([m, g])
    out["data_points"] = pts
    out["num_points"] = len(pts)
    out["is_new_limit"] = bool(raw.get("is_new_limit")) if raw.get("is_new_limit") is not None else bool(pts)
    out["is_projection"] = bool(raw.get("is_projection", False))
    if out["data_source"] is None:
        out["data_source"] = "none" if not pts else "unknown"
    for k in ("confidence_level", "extraction_confidence", "dm_density_assumed"):
        v = out.get(k)
        if v is not None:
            try:
                out[k] = float(v)
            except (TypeError, ValueError):
                problems.append(f"non-numeric {k}={v!r}")
                out[k] = None
    if out["confidence_level"] is None:
        out["confidence_level"] = 0.95
    if out["extraction_confidence"] is None:
        out["extraction_confidence"] = 0.5
    for k in ("paper_title", "suggested_experiment_name", "notes", "coupling_convention"):
        if out.get(k) is not None and not isinstance(out[k], str):
            out[k] = json.dumps(out[k])
    return out, problems


def write_json(path: Path, obj) -> None:
    """Atomic write: a reader (or a second driver) never sees a partial file."""
    tmp = path.with_suffix(path.suffix + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(obj, indent=1))
    os.replace(tmp, path)


def snapshot_kind(d: dict) -> str:
    if d.get("status") == "error" or d.get("error"):
        return "error"
    return "good"


def run_paper(aid: str, args, transport: Transport, task_card: str,
              task_card_sha: str) -> tuple[str, str]:
    sid = safe_id(aid)
    outdir = Path(args.outdir)
    dest = outdir / f"{sid}.json"
    if dest.exists():
        try:
            kind = snapshot_kind(json.loads(dest.read_text()))
        except Exception:
            kind = "error"
        if kind == "good":
            return aid, "cached"
        dest.unlink()

    pdf = None
    for cand in (Path(args.pdf_cache) / f"{sid}.pdf", Path(args.pdf_cache) / f"{aid}.pdf"):
        if cand.exists():
            pdf = cand
            break
    if pdf is None:
        write_json(dest, {"arxiv_id": aid, "status": "error",
                                    "error": "PDF not in cache"})
        return aid, "error: PDF not in cache"

    work = outdir / "work" / sid
    argv = build_argv(args, task_card)
    prompt = user_prompt(aid, work)

    for attempt in range(8):
        if work.exists():
            shutil.rmtree(work, ignore_errors=True)
        work.mkdir(parents=True)
        shutil.copyfile(pdf, work / "paper.pdf")
        env = transport.child_env()
        mode = transport.mode
        t0 = time.time()
        timed_out = False
        try:
            proc = subprocess.run(argv, input=prompt, text=True, capture_output=True,
                                  cwd=work, env=env, timeout=args.timeout_s)
            stdout, stderr, rc = proc.stdout, proc.stderr, proc.returncode
        except subprocess.TimeoutExpired as e:
            timed_out = True
            stdout = (e.stdout.decode() if isinstance(e.stdout, bytes) else e.stdout) or ""
            stderr = (e.stderr.decode() if isinstance(e.stderr, bytes) else e.stderr) or ""
            rc = -9
        elapsed = time.time() - t0
        events, result_ev = parse_events(stdout)
        events_path = outdir / f"{sid}.events.jsonl"
        events_path.write_text("\n".join(json.dumps(e) for e in events) + "\n")

        err_text = ""
        if result_ev is None:
            err_text = f"{stderr}\n{stdout[-2000:]}"
        elif result_ev.get("is_error") or result_ev.get("subtype") not in (None, "success"):
            err_text = f"{stderr}\n{result_ev.get('result', '')}\n{result_ev.get('subtype', '')}"

        if err_text and not timed_out:
            kind = classify_error_text(err_text)
            if kind == "usage_limit":
                transport.on_usage_limit(err_text)
                continue
            if kind == "fatal":
                raise FatalRunError(err_text.strip()[:400])
            if kind == "rate":
                delay = 60 * (attempt + 1)
                log(f"{aid}: rate/overload, backing off {delay}s")
                time.sleep(delay)
                continue
            # Budget cap or max-turn style terminations still leave result.json
            # if the agent got that far; fall through and use whatever exists.

        # The CLI's shell keeps its cwd between Bash calls, so an agent that
        # `cd`s into the unpacked e-print writes ./result.json there. The
        # answer is still the answer: take the top-level file if present,
        # else the shallowest result.json anywhere under the work dir.
        result_path = work / "result.json"
        if not result_path.exists():
            found = sorted(work.rglob("result.json"), key=lambda q: len(q.parts))
            if found:
                result_path = found[0]
                problems_note = f"result.json found at {result_path.relative_to(work)}"
            else:
                problems_note = None
        else:
            problems_note = None
        raw = None
        problems: list[str] = [problems_note] if problems_note else []
        if result_path.exists():
            try:
                raw = json.loads(result_path.read_text())
                if not isinstance(raw, dict):
                    problems.append("result.json is not an object")
                    raw = None
            except json.JSONDecodeError as e:
                problems.append(f"result.json unparseable: {e}")

        if raw is None and err_text and not timed_out:
            # Genuine paper-level failure with no answer: error stub (retried
            # on resume, not counted as an answer).
            write_json(dest, {
                "arxiv_id": aid, "status": "error",
                "error": err_text.strip()[:600],
                "meta": {"transport": mode, "elapsed_s": elapsed, "attempt": attempt},
            })
            return aid, f"error: {err_text.strip()[:80]}"

        snap, norm_problems = normalise_result(raw or {})
        problems += norm_problems
        usage = (result_ev or {}).get("usage") or {}
        model_usage = (result_ev or {}).get("modelUsage") or {}
        models_billed = sorted(model_usage.keys())
        if args.strict_model and models_billed and not any(
                m == args.model or m.startswith(args.model) for m in models_billed):
            raise FatalRunError(
                f"silent model substitution: requested {args.model}, billed {models_billed}")
        leaks = scan_leaks(events_path.read_text())
        snap.update({
            "arxiv_id": aid,
            "elapsed_s": elapsed,
            "meta": {
                "system": "agent_claude_code",
                "driver_version": DRIVER_VERSION,
                "task_card_sha256": task_card_sha,
                "model_requested": args.model,
                "models_billed": models_billed,
                "effort": args.effort or "default",
                "transport": mode,
                "timed_out": timed_out,
                "wrote_result_json": raw is not None,
                "cli_is_error": bool((result_ev or {}).get("is_error")),
                "cli_subtype": (result_ev or {}).get("subtype"),
                "cli_returncode": rc,
                "num_turns": (result_ev or {}).get("num_turns"),
                "duration_ms": (result_ev or {}).get("duration_ms"),
                "duration_api_ms": (result_ev or {}).get("duration_api_ms"),
                "total_cost_usd": (result_ev or {}).get("total_cost_usd"),
                "usage": {k: usage.get(k) for k in (
                    "input_tokens", "output_tokens",
                    "cache_creation_input_tokens", "cache_read_input_tokens")},
                "leak_suspect": bool(leaks),
                "leak_patterns": leaks,
                "schema_problems": problems,
                "events_file": events_path.name,
                "attempt": attempt,
                "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            },
        })
        write_json(dest, snap)
        if not args.keep_work:
            shutil.rmtree(work, ignore_errors=True)
        tag = ("TIMEOUT " if timed_out else "") + ("LEAK? " if leaks else "")
        return aid, (f"{tag}{elapsed:.0f}s ct={snap.get('coupling_type')} "
                     f"n={snap['num_points']} src={snap.get('data_source')} "
                     f"turns={snap['meta']['num_turns']} "
                     f"${snap['meta']['total_cost_usd'] or 0:.2f} via {mode}")

    write_json(dest, {"arxiv_id": aid, "status": "error",
                                "error": "exhausted attempts"})
    return aid, "error: exhausted attempts"


def preflight(args, transport: Transport) -> None:
    """1-token ping. On a logged-out CLI with an API key available, switch
    straight to API billing; with nothing available, abort with instructions."""
    argv = [args.claude_bin, "-p", "--model", args.model, "--tools", "",
            "--output-format", "json", "--no-session-persistence",
            "--setting-sources", "", "--strict-mcp-config"]
    for _ in range(2):
        proc = subprocess.run(argv, input="Reply with the single word pong.",
                              text=True, capture_output=True,
                              env=transport.child_env(), timeout=180)
        try:
            d = json.loads(proc.stdout)
        except json.JSONDecodeError:
            d = {"is_error": True, "result": proc.stderr + proc.stdout}
        if not d.get("is_error"):
            log(f"preflight OK via {transport.mode}; billed models {sorted((d.get('modelUsage') or {}).keys())}")
            return
        text = str(d.get("result", ""))
        kind = classify_error_text(text)
        if kind == "usage_limit" or (kind == "fatal" and "log" in text.lower()):
            if transport.mode == "cli" and transport.api_key():
                log(f"CLI unavailable ({text[:80]!r}); switching to API billing now")
                with transport.lock:
                    transport.mode = "api"
                    transport.switched_at = time.time()
                continue
            if kind == "usage_limit":
                transport.on_usage_limit(text)
                continue
        raise FatalRunError(
            f"preflight failed via {transport.mode}: {text[:200]}\n"
            f"  - subscription: run `claude login` in a terminal\n"
            f"  - credit: put the API key in {transport.key_file} (chmod 600) or export AXLB_API_KEY")
    raise FatalRunError("preflight failed twice")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--ids-file", default=str(DEFAULT_IDS))
    ap.add_argument("--ids", default=None, help="comma-separated arXiv ids (overrides --ids-file)")
    ap.add_argument("--limit", type=int, default=None, help="only the first N ids")
    ap.add_argument("--model", default="claude-fable-5")
    ap.add_argument("--effort", default=None, help="CLI --effort (default: CLI default)")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--timeout-s", type=int, default=1800)
    ap.add_argument("--max-budget-usd", type=float, default=None,
                    help="per-paper spend cap passed to the CLI; the benchmark itself imposes none (our pre-submission reference run used 10)")
    ap.add_argument("--transport", choices=("auto", "cli", "api"), default="auto")
    ap.add_argument("--api-key-file", default=str(DEFAULT_KEY_FILE))
    ap.add_argument("--pdf-cache", default=str(Path.home() / ".cache" / "aal_pdf_cache"))
    ap.add_argument("--claude-bin", default="claude")
    ap.add_argument("--keep-work", action="store_true")
    ap.add_argument("--no-strict-model", dest="strict_model", action="store_false")
    args = ap.parse_args()

    task_card = TASK_CARD_PATH.read_text()
    task_card_sha = hashlib.sha256(task_card.encode()).hexdigest()
    if args.ids:
        ids = [i.strip() for i in args.ids.split(",") if i.strip()]
    else:
        ids = json.loads(Path(args.ids_file).read_text())
    if args.limit:
        ids = ids[: args.limit]
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    # Single-writer lock. Two drivers on one outdir race on snapshot writes
    # (observed 2026-09-16: concurrent instances produced a snapshot with a
    # stray trailing brace, plus duplicate extractions billed twice).
    lock = outdir / ".driver.lock"
    try:
        fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
    except FileExistsError:
        holder = lock.read_text().strip() or "?"
        alive = True
        try:
            os.kill(int(holder), 0)
        except (ValueError, ProcessLookupError):
            alive = False
        except PermissionError:
            alive = True
        if alive:
            log(f"FATAL: another driver (pid {holder}) is already writing {outdir}; "
                f"stop it first, or delete {lock} if it is stale")
            return 4
        log(f"removing stale lock from pid {holder}")
        lock.write_text(str(os.getpid()))
    atexit.register(lambda: lock.unlink(missing_ok=True))

    transport = Transport("api" if args.transport == "api" else "cli", Path(args.api_key_file))
    run_meta = {
        "system": "agent_claude_code", "driver_version": DRIVER_VERSION,
        "model": args.model, "effort": args.effort or "default",
        "task_card_sha256": task_card_sha, "workers": args.workers,
        "timeout_s": args.timeout_s, "max_budget_usd": args.max_budget_usd,
        "transport_start": transport.mode, "n_ids": len(ids),
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "claude_version": subprocess.run([args.claude_bin, "--version"], capture_output=True,
                                         text=True).stdout.strip(),
    }
    (outdir / "run.json").write_text(json.dumps(run_meta, indent=1))
    log(f"run: {json.dumps(run_meta)}")

    try:
        preflight(args, transport)
    except FatalRunError as e:
        log(f"FATAL: {e}")
        return 3

    done = 0
    total_cost = 0.0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(run_paper, aid, args, transport, task_card, task_card_sha): aid for aid in ids}
        try:
            for f in as_completed(futs):
                aid, msg = f.result()
                done += 1
                try:
                    total_cost += float(json.loads((outdir / f"{safe_id(aid)}.json").read_text())
                                        .get("meta", {}).get("total_cost_usd") or 0)
                except Exception:
                    pass
                log(f"[{done}/{len(ids)}] {aid}: {msg}   (cum ${total_cost:.2f}, transport={transport.mode})")
        except FatalRunError as e:
            log(f"FATAL availability error: {e}")
            ex.shutdown(wait=False, cancel_futures=True)
            return 2
    run_meta.update({"finished_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                     "transport_end": transport.mode,
                     "switched_at": transport.switched_at,
                     "total_cost_usd_reported": total_cost})
    (outdir / "run.json").write_text(json.dumps(run_meta, indent=1))
    log("ALL DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
