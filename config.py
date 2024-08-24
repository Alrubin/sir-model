from dataclasses import dataclass

from plotly.graph_objs import Layout


layout = Layout(
    plot_bgcolor="#f8f9fa",
    margin={"b": 0, "l": 20, "r": 20, "t": 0},
    title={'y': 0.98, 'x': 0.08, 'xanchor': "left", 'yanchor': "top"},
    height=350,
    yaxis_title="Popolazione",
    font={"size": 18},
    legend={
        'orientation': "h",
        'yanchor': "bottom",
        'y': 1,
        'xanchor': "right",
        'x': 1.02
    }
)
