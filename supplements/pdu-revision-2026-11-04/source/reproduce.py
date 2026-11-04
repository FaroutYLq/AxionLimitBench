"""Reproduce the revised PDU evaluation offline, without extraction/model calls.

Usage: python reproduce.py --out /absolute/path/to/new-output-directory
Requires both compact analysis and transcript archives extracted together.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path)
    ap.add_argument('--figures', action='store_true', help='Also rebuild all Python figures (showcase requires LaTeX).')
    args = ap.parse_args()
    root = Path(__file__).resolve().parent
    out = args.out.resolve() if args.out else Path(tempfile.mkdtemp(prefix='pdu-reproduction-'))
    if out == root or root in out.parents:
        ap.error('Output must be outside the release input directory.')
    out.mkdir(parents=True, exist_ok=True)
    work = out / 'work'
    assert not work.exists(), 'Use a fresh output directory.'
    shutil.copytree(root, work, ignore=shutil.ignore_patterns('benchmark', '__pycache__', '*.pyc'))
    env = dict(os.environ, AXLB_BENCHMARK_ROOT=str(root / 'benchmark'), PYTHONDONTWRITEBYTECODE='1',
               MPLCONFIGDIR=str(out / 'mpl-cache'))
    commands = []

    def run(name, argv, cwd=work):
        result = subprocess.run(argv, cwd=cwd, env=env, text=True, capture_output=True)
        (out / (name + '.log')).write_text(result.stdout + '\n' + result.stderr)
        commands.append({'step': name, 'command': argv, 'returncode': result.returncode})
        print(name, 'OK' if result.returncode == 0 else 'FAILED', flush=True)
        if result.returncode:
            raise RuntimeError(result.stderr[-2000:] or result.stdout[-2000:])

    run('coverage', [sys.executable, '-m', 'evaluation.revision.ml4ps_coverage',
                    '--benchmark-root', str(root / 'benchmark'), '--old-report',
                    str(work / 'paper/revision/cohort_coverage')])
    checks = []

    def same_json(rel):
        a, b = json.loads((root / rel).read_text()), json.loads((work / rel).read_text())
        assert a == b, rel
        checks.append({'artifact': rel, 'check': 'Exact parsed-JSON equality', 'passed': True})

    for name in ['summary.json', 'per_paper.json', 'cohorts.json', 'excluded_cases.json']:
        same_json('paper/revision/ml4ps_coverage/' + name)
    run('disposition', [sys.executable, 'paper/revision/disposition_audit/analyze.py'])
    same_json('paper/revision/disposition_audit/fable_outcomes.json')
    run('table', [sys.executable, 'paper/revision/tables/table2_preview/make_table.py'])
    same_json('paper/revision/tables/table2_preview/table2_data.json')
    repeat = work / 'paper/revision/repeatability_fable5_agent_100papers'
    run('repeatability', [sys.executable, str(repeat / 'analysis/analyze.py'),
                         '--out', str(repeat / 'analysis'), '--scoring-dir', str(repeat / 'scoring')])
    rel = 'paper/revision/repeatability_fable5_agent_100papers/analysis/summary.json'
    a, b = json.loads((root / rel).read_text()), json.loads((work / rel).read_text())
    # Paths are expected to change; all statistical fields must agree exactly.
    for key in a:
        if key not in {'scorer', 'run_meta'}:
            assert a[key] == b[key], ('repeatability', key)
    checks.append({'artifact': rel, 'check': 'All statistics equal; relocated scorer path excluded', 'passed': True})
    if args.figures:
        for name in ['figure2_showcase_preview', 'figure4_residual_cdf_preview',
                     'figure5_per_type_preview', 'figureF1_calibration_preview', 'figureF2_repeatability_preview']:
            run(name, [sys.executable, f'paper/revision/figures/{name}/make_figure.py'])
        run('coverage_figure', [sys.executable, 'paper/revision/ml4ps_coverage/make_pdu_coverage_figure.py'])
    report = {'status': 'passed', 'commands': commands, 'checks': checks,
              'no_model_calls': True, 'no_network_required': True}
    (out / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print('Verified:', out / 'verification.json')


if __name__ == '__main__':
    main()
