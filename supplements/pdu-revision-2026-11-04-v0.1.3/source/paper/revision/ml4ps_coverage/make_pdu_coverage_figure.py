"""Manuscript-sized version of the approved histogram, using frozen bins."""
import json
import os
from pathlib import Path

import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'aal-pdu-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / 'coverage_both_histograms_linear_bins.json').read_text())
plt.rcParams.update({'font.size': 9, 'pdf.fonttype': 42, 'axes.grid': True,
                     'grid.alpha': .3, 'axes.axisbelow': True})
fig, axes = plt.subplots(2, 3, figsize=(6.5, 4.6), sharex=True, sharey=True)
models = [('fable', 'Fable 5', '#c0392b', '#1f4e79'),
          ('opus', 'Opus 4.8', '#e67e22', '#2e86c1'),
          ('haiku', 'Haiku 4.5', '#d7a86e', '#7f8c8d')]
edges = np.asarray(data['bin_edges'])
for col, (key, name, agent_color, pipeline_color) in enumerate(models):
    for row, measure in enumerate(['reference', 'extraction']):
        ax = axes[row, col]
        for offset, arm, color in [(0, 'agent', agent_color), (4.6, 'pipeline', pipeline_color)]:
            values = data['arms'][f'{arm}_{key}']
            hist = values[measure]
            assert sum(hist['counts']) + hist['na'] == values['n']
            assert np.allclose(np.asarray(hist['counts']) / values['n'], hist['fractions'])
            label = f"{arm} (n={values['n']}"
            if row:
                label += f"; N/A={hist['na']}"
            label += ')'
            ax.bar(edges[:-1] + .4 + offset, hist['fractions'], width=4.6,
                   align='edge', color=color, edgecolor='white', linewidth=.3,
                   label=label)
        ax.axvline(90, color='.45', linestyle='-.', linewidth=.7)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 1)
        ax.set_xticks(np.arange(0, 101, 20))
        ax.set_yticks(np.arange(0, 1.01, .2))
        ax.tick_params(labelsize=8, labelbottom=True)
        ax.set_xlabel(r'$C_{\rm ref}$ [%]' if row == 0 else r'$C_{\rm ext}$ [%]')
        ax.legend(loc='upper left', fontsize=7, handlelength=1.1,
                  handletextpad=.4, borderpad=.35)
        if row == 0:
            ax.set_title(name, fontsize=10)
        if col == 0:
            ax.set_ylabel(f'{measure} denominator\nfraction of papers in bin', fontsize=8)
fig.tight_layout(w_pad=.8, h_pad=1.2)
fig.savefig(HERE / 'coverage_pdu.png', dpi=300, bbox_inches='tight')
fig.savefig(HERE.parents[1] / 'figures' / 'coverage_agent_pipeline.pdf', bbox_inches='tight')
plt.close(fig)
