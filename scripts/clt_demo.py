"""
Generates the CLT demo chart for the sample article.
Run from the scripts/ directory: uv run python clt_demo.py
Output: ../public/charts/clt-demo.json
"""
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

np.random.seed(42)
N_SIMS = 5000
SAMPLE_SIZES = [1, 5, 20, 100]
ACCENT = "#7b79f7"
RED = "#f87171"

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=[f"n = {n}" for n in SAMPLE_SIZES],
    horizontal_spacing=0.12,
    vertical_spacing=0.18,
)

for i, n in enumerate(SAMPLE_SIZES):
    row, col = i // 2 + 1, i % 2 + 1

    # Sample means from Exp(1) — deliberately non-normal source distribution
    means = np.random.exponential(1, size=(N_SIMS, n)).mean(axis=1)
    standardized = (means - 1) / (1 / np.sqrt(n))

    fig.add_trace(go.Histogram(
        x=standardized,
        histnorm="probability density",
        nbinsx=60,
        marker_color=ACCENT,
        opacity=0.75,
        showlegend=(i == 0),
        name="Sample means",
    ), row=row, col=col)

    x = np.linspace(-4, 4, 300)
    y = np.exp(-(x ** 2) / 2) / np.sqrt(2 * np.pi)
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode="lines",
        line=dict(color=RED, width=2.5),
        showlegend=(i == 0),
        name="N(0, 1)",
    ), row=row, col=col)

    fig.update_xaxes(range=[-4, 4], row=row, col=col)

fig.update_layout(
    title=dict(
        text="Standardized sample means from Exp(1) converge to N(0, 1)",
        font=dict(size=14),
    ),
    height=480,
    template="plotly_white",
    legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.08),
    margin=dict(t=80, b=60, l=40, r=40),
)

out = Path(__file__).parent.parent / "public" / "charts" / "clt-demo.json"
out.write_text(fig.to_json())
print(f"Wrote {out}")
