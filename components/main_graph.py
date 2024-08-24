from typing import List

from dash import dcc
from plotly import graph_objects as go

from plotly.graph_objs import Layout

from lib.population import Population


class ScatterLine(go.Scatter):
    def __init__(self, days: list[float], values: list[float], name: str, color: str):
        super().__init__(
            x=days,
            y=values,
            mode='lines',
            name=name,
            line={'color': color, 'width': 3}
        )


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


class MainGraph(go.Figure):
    def __init__(self, lines: list[ScatterLine], layout: Layout):
        super().__init__(
            data=lines,
            layout=layout
        )


def update_graph(population_evolution: List[Population]):
    susceptibles = [population.susceptibles for population in population_evolution]
    infected = [population.infected for population in population_evolution]
    removed = [population.removed for population in population_evolution]
    giorni = list(range(len(population_evolution) + 1))

    fig = MainGraph([
        ScatterLine(giorni, susceptibles, 'Suscettibili', 'royalblue'),
        ScatterLine(giorni, infected, 'Infetti', 'red'),
        ScatterLine(giorni, removed, 'Rimossi', 'green')
    ],
        layout
    )

    return dcc.Graph(figure=fig)
