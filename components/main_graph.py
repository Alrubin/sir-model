from dash import dcc
from plotly import graph_objects as go

from config import GraphLayoutSettings


class ScatterLine(go.Scatter):
    def __init__(self, days: list[float], values: list[float], name: str, color: str):
        super().__init__(
            x=days,
            y=values,
            mode='lines',
            name=name,
            line={'color': color, 'width': 3}
        )


class MainGraph(go.Figure):
    def __init__(self, lines: list[ScatterLine], layout: GraphLayoutSettings):
        super().__init__(
            data=lines,
            layout={'plot_bgcolor': layout.background_color,
                    'margin': {"b": layout.margin_bottom,
                               "l": layout.margin_left,
                               "r": layout.margin_right,
                               "t": layout.margin_top},
                    'title': {'y': layout.title_y,
                              'x': layout.title_x,
                              'xanchor': layout.title_xanchor,
                              'yanchor': layout.title_yanchor},
                    'height': layout.height,
                    'yaxis_title': layout.title,
                    'font': {"size": layout.font_size},
                    'legend': {'orientation': layout.legend_orientation,
                               'yanchor': layout.legend_yanchor,
                               'y': layout.legend_yaxis,
                               'xanchor': layout.legend_xanchor,
                               'x': layout.legend_yaxis}}
        )
