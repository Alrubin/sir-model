from dash import dcc
from plotly import graph_objects as go

from config import GraphLayoutSettings


class ScatterLine:
    def __init__(self, days: list[float], values: list[float], name: str, color: str):
        self.days = days
        self.values = values
        self.name = name
        self.color = color

    def figure(self):
        return go.Scatter(
            x=self.days,
            y=self.values,
            mode='lines',
            name=self.name,
            line={'color': self.color, 'width': 3}
        )


class MainGraph:
    def __init__(self, lines: list[ScatterLine], layout: GraphLayoutSettings):
        self.lines = lines
        self.layout = layout

    def build(self):
        fig = go.Figure()
        for line in self.lines:
            fig.add_trace(line.figure())
        fig.update_layout(
            overwrite=self.layout.overwrite,
            plot_bgcolor=self.layout.background_color,
            margin={"b": self.layout.margin_bottom,
                    "l": self.layout.margin_left,
                    "r": self.layout.margin_right,
                    "t": self.layout.margin_top},
            title={'y': self.layout.title_y,
                   'x': self.layout.title_x,
                   'xanchor': self.layout.title_xanchor,
                   'yanchor': self.layout.title_yanchor},
            height=self.layout.height,
            yaxis_title=self.layout.title,
            font={"size": self.layout.font_size},
            legend={'orientation': self.layout.legend_orientation,
                    'yanchor': self.layout.legend_yanchor,
                    'y': self.layout.legend_yaxis,
                    'xanchor': self.layout.legend_xanchor,
                    'x': self.layout.legend_yaxis}
        )

        return dcc.Graph(figure=fig)
