#!/usr/bin/env python3
"""Two fresh, independent agent sessions per paper, interleaved across papers.

This is a SCHEDULER ONLY. Every session is executed by the frozen benchmark
driver's own ``run_paper`` (baselines/agent_claude_code/run_agent.py at commit
ac15429), imported unmodified: same argv (model, tools allow-list, permission
deny-list, --max-budget-usd, timeout), same user prompt, same task card
(docs/TASK.md), same normalisation, leak audit and snapshot format. The only
things this file adds are (a) two output directories, (b) an interleaved work
queue [(p1,r1),(p1,r2),(p2,r1),(p2,r2),...] over a shared 3-worker pool, and
(c) an attempt log with timestamps.

Billing: transport is pinned to "cli" (the Claude Code subscription OAuth).
No API key is placed in the environment or key file, so the driver can never
fail over to API-key billing: on a usage-limit error it PAUSES (polls for a
key every 60 s) and the pause is visible in the log.
"""
import argparse, hashlib, json, os, platform, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

FROZEN = Path("/private/tmp/axionlimitbench-revision-source")
sys.path.insert(0, str(FROZEN / "baselines" / "agent_claude_code"))
import run_agent as RA  # noqa: E402  frozen driver, unmodified

EXP = Path(__file__).resolve().parents[1]
SEL = json.loads((EXP / "protocol" / "selected_ids.json").read_text())
IDS = SEL["ids_in_draw_order"]
REPEATS = ("repeat1", "repeat2")


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    ids = IDS[: a.limit] if a.limit else IDS

    # Benchmark Fable configuration (results/agent_claude_code/fable5/run.json):
    # model claude-fable-5, effort default (no --effort), timeout 1800 s,
    # --max-budget-usd 10, transport cli, workers 3, PDF cache ~/.cache/aal_pdf_cache.
    common = dict(model="claude-fable-5", effort=None, timeout_s=1800, max_budget_usd=10.0,
                  transport="cli", api_key_file=str(RA.DEFAULT_KEY_FILE),
                  pdf_cache=str(Path.home() / ".cache" / "aal_pdf_cache"),
                  claude_bin="claude", keep_work=False, strict_model=True, workers=a.workers)
    for k in ("ANTHROPIC_API_KEY", "AXLB_API_KEY"):
        assert not os.environ.get(k), f"{k} is set: refuse to run (would enable silent API failover)"
    assert not Path(common["api_key_file"]).exists(), "API key file exists: refuse to run"

    task_card = RA.TASK_CARD_PATH.read_text()
    task_card_sha = hashlib.sha256(task_card.encode()).hexdigest()
    args_by_rep = {}
    for rep in REPEATS:
        od = EXP / "runs" / rep
        od.mkdir(parents=True, exist_ok=True)
        lock = od / ".driver.lock"
        if lock.exists():
            print(f"FATAL: lock exists {lock}"); return 4
        lock.write_text(str(os.getpid()))
        args_by_rep[rep] = argparse.Namespace(outdir=str(od), **common)

    transport = RA.Transport("cli", Path(common["api_key_file"]))
    claude_version = subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
    pdf_sha = {}
    for aid in ids:
        sid = RA.safe_id(aid)
        for cand in (Path(common["pdf_cache"]) / f"{sid}.pdf", Path(common["pdf_cache"]) / f"{aid}.pdf"):
            if cand.exists():
                pdf_sha[aid] = {"file": str(cand), "sha256": sha256(cand), "bytes": cand.stat().st_size}
                break
        else:
            print(f"FATAL: no cached PDF for {aid}"); return 5
    run_meta = {
        "experiment": "fable5_agent_repeatability_100papers",
        "scheduler": str(Path(__file__).resolve()),
        "scheduler_sha256": sha256(Path(__file__).resolve()),
        "frozen_source": str(FROZEN), "frozen_commit": SEL["frozen_commit"],
        "run_agent_path": str(FROZEN / "baselines/agent_claude_code/run_agent.py"),
        "run_agent_sha256": sha256(FROZEN / "baselines/agent_claude_code/run_agent.py"),
        "driver_version": RA.DRIVER_VERSION,
        "task_card_path": str(RA.TASK_CARD_PATH), "task_card_sha256": task_card_sha,
        "selected_ids_sha256": sha256(EXP / "protocol" / "selected_ids.json"),
        "argv_template": RA.build_argv(args_by_rep["repeat1"], "<TASK_CARD>"),
        "allowed_tools": RA.ALLOWED_TOOLS, "settings": RA.SETTINGS,
        "config": {k: v for k, v in common.items()},
        "n_papers": len(ids), "n_sessions_planned": 2 * len(ids),
        "queue_order": "interleaved: (paper_i, repeat1), (paper_i, repeat2), paper_i+1 ...",
        "claude_version": claude_version,
        "python": sys.version.split()[0], "platform": platform.platform(),
        "host": platform.node(),
        "launch_note": os.environ.get("RUN_REPEATS_NOTE"),
        "snapshots_present_at_launch": {rep: sorted(q.stem for q in (EXP / "runs" / rep).glob("*.json")) for rep in REPEATS},
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "started_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "pdf_inputs": pdf_sha,
    }
    (EXP / "runs" / "run.json").write_text(json.dumps(run_meta, indent=1))
    RA.log(f"run: {json.dumps({k: v for k, v in run_meta.items() if k != 'pdf_inputs'})}")

    try:
        RA.preflight(args_by_rep["repeat1"], transport)
    except RA.FatalRunError as e:
        RA.log(f"FATAL preflight: {e}"); return 3
    if transport.mode != "cli":
        RA.log("FATAL: transport is not cli after preflight"); return 3

    attempts = EXP / "runs" / "attempts.jsonl"
    alock = threading.Lock()

    def job(aid, rep):
        t0 = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        aid_, msg = RA.run_paper(aid, args_by_rep[rep], transport, task_card, task_card_sha)
        rec = {"arxiv_id": aid, "repeat": rep, "started_at": t0,
               "finished_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "outcome": msg,
               "transport": transport.mode}
        with alock:
            with attempts.open("a") as f:
                f.write(json.dumps(rec) + "\n")
        return aid, rep, msg

    queue = [(aid, rep) for aid in ids for rep in REPEATS]
    done, cost = 0, 0.0
    rc = 0
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = [ex.submit(job, aid, rep) for aid, rep in queue]
        try:
            for f in as_completed(futs):
                aid, rep, msg = f.result()
                done += 1
                try:
                    cost += float(json.loads((EXP / "runs" / rep / f"{RA.safe_id(aid)}.json").read_text())
                                  .get("meta", {}).get("total_cost_usd") or 0)
                except Exception:
                    pass
                RA.log(f"[{done}/{len(queue)}] {aid} {rep}: {msg}   (cum ${cost:.2f}, transport={transport.mode})")
        except RA.FatalRunError as e:
            RA.log(f"FATAL availability error: {e}")
            ex.shutdown(wait=False, cancel_futures=True)
            rc = 2
    run_meta.update({"finished_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                     "finished_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                     "transport_end": transport.mode, "switched_at": transport.switched_at,
                     "sessions_completed": done, "total_cost_usd_reported": cost, "exit_code": rc})
    (EXP / "runs" / "run.json").write_text(json.dumps(run_meta, indent=1))
    for rep in REPEATS:
        (EXP / "runs" / rep / ".driver.lock").unlink(missing_ok=True)
    RA.log("ALL DONE" if rc == 0 else f"EXIT {rc}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
