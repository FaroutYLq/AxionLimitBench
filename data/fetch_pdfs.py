#!/usr/bin/env python3
"""Download the benchmark papers' PDFs from arXiv (they are not redistributed).

    python3 data/fetch_pdfs.py --out ~/.cache/axionlimitbench/pdfs            # measured-limit pool (329)
    python3 data/fetch_pdfs.py --out DIR --all                                   # full pool (347)
    python3 data/fetch_pdfs.py --out DIR --ids 2208.07293,hep-ph/0307284

Files are named <id>.pdf with "/" replaced by "_" (hep-ph/0307284 -> hep-ph_0307284.pdf).
Existing files are kept. arXiv rate-limits bursts, so the default is one download
every 3 s with retries; expect ~20 min for the full pool.

Version note: arXiv serves the LATEST version at /pdf/<id>. The reference curves were
digitised from whatever version the compilation maintainer used (see the audit in
results/agent_claude_code/fable5_failure_audit_2x.json for known stale entries); AxionLimitBench will
pin versions per paper. To pin a version yourself use --version-suffix, e.g. v2.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def fetch(aid: str, dest: Path, retries: int = 5, delay: float = 3.0, version_suffix: str = "") -> str:
    url = f"https://arxiv.org/pdf/{aid}{version_suffix}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "AxionLimitBench/0.1 (benchmark PDF fetch)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if not data.startswith(b"%PDF"):
                raise ValueError("response is not a PDF (arXiv may have returned an HTML notice)")
            dest.write_bytes(data)
            return hashlib.sha256(data).hexdigest()
        except (urllib.error.HTTPError, urllib.error.URLError, ValueError, TimeoutError) as e:
            wait = delay * (2 ** attempt)
            print(f"  {aid}: attempt {attempt + 1} failed ({e}); retrying in {wait:.0f}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"could not fetch {aid}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--all", action="store_true", help="full 347-paper pool instead of the 329 measured-limit pool")
    ap.add_argument("--ids", default=None, help="comma-separated arXiv ids (overrides the pool)")
    ap.add_argument("--delay", type=float, default=3.0)
    ap.add_argument("--version-suffix", default="", help='e.g. "v2" to pin a version for every id (rarely wanted)')
    args = ap.parse_args()

    if args.ids:
        ids = [i.strip() for i in args.ids.split(",") if i.strip()]
    elif args.all:
        ids = [p["arxiv_id"] for p in json.loads((ROOT / "data/manifest.json").read_text())["papers"]]
    else:
        ids = json.loads((ROOT / "data/measured_pool_ids.json").read_text())
    out = Path(args.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    manifest = out / "sha256.json"
    sums = json.loads(manifest.read_text()) if manifest.exists() else {}
    for n, aid in enumerate(ids, 1):
        dest = out / f"{aid.replace('/', '_')}.pdf"
        if dest.exists() and dest.stat().st_size > 0:
            print(f"[{n}/{len(ids)}] {aid}: cached")
            continue
        sums[aid] = fetch(aid, dest, delay=args.delay, version_suffix=args.version_suffix)
        manifest.write_text(json.dumps(sums, indent=1, sort_keys=True))
        print(f"[{n}/{len(ids)}] {aid}: {dest.stat().st_size // 1024} kB")
        time.sleep(args.delay)
    print(f"done: {len(ids)} papers in {out}; sha256 manifest at {manifest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
