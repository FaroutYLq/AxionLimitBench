"""Re-audit agent transcripts for forbidden-source access with the strict rule
(only what the agent issued or said counts) and rewrite meta.leak_suspect /
meta.leak_patterns in each snapshot. Also records what each flagged agent
actually did so a human can judge.

    python3 baselines/agent_claude_code/audit_leaks.py results/agent_claude_code/fable5
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_agent import scan_leaks  # noqa: E402


def main(run_dir: str) -> None:
    d = Path(run_dir)
    changed = flagged = 0
    for snap in sorted(d.glob("*.json")):
        if snap.name in ("run.json", "metrics.json", "metrics_summary.json"):
            continue
        s = json.loads(snap.read_text())
        meta = s.get("meta")
        if not meta:
            continue
        ev = d / meta.get("events_file", f"{snap.stem}.events.jsonl")
        if not ev.exists():
            continue
        hits = scan_leaks(ev.read_text())
        new = {"leak_suspect": bool(hits), "leak_patterns": hits, "leak_audit": "strict-v2 (agent-issued only)"}
        if any(meta.get(k) != v for k, v in new.items()):
            meta.update(new)
            snap.write_text(json.dumps(s, indent=1))
            changed += 1
        if hits:
            flagged += 1
            print(f"FLAG {snap.stem}: {hits}")
    print(f"audited {run_dir}: {changed} snapshots updated, {flagged} flagged under the strict rule")


if __name__ == "__main__":
    main(sys.argv[1])
