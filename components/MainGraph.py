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


class MainGraph(dcc.Graph):
    def __init__(self, population_evolution: List[Population], layout: Layout):
        self.susceptibles = [population.susceptibles for population in population_evolution]
        self.infected = [population.infected for population in population_evolution]
        self.removed = [population.removed for population in population_evolution]
        self.giorni = list(range(len(population_evolution) + 1))
        self.layout = layout

        self.fig = go.Figure(data=[
            ScatterLine(self.giorni, self.susceptibles, 'Suscettibili', 'royalblue'),
            ScatterLine(self.giorni, self.infected, 'Infetti', 'red'),
            ScatterLine(self.giorni, self.removed, 'Rimossi', 'green')
        ],
            layout=self.layout
        )
        super().__init__(figure=self.fig)
