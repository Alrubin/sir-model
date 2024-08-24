from typing import Union
import numpy as np
from plotly.graph_objs import Layout
from scipy.integrate import odeint

from components.MainGraph import MainGraph
from lib.disease import SIRDisease
from lib.model import SIRModel
from lib.population import InitialValues, Population


class SIRScenario:
    def __init__(self, initial_conditions: InitialValues, disease: Union[None, SIRDisease] = None):
        self.initial_conditions = initial_conditions
        self.disease = disease
        self._model = SIRModel(disease=self.disease)

    def compute_evolution(self, n_days) -> list[Population]:
        initial_conditions = np.array(self.initial_conditions).reshape(1, -1)
        time_grid = np.linspace(start=0, stop=n_days, num=n_days)
        population_evolution = odeint(self._model, self.initial_conditions, time_grid)

        return [Population(*population) for population in np.vstack((initial_conditions, population_evolution))]


def update_scenario(S0, I0, R0, n_days):
    initial_conditions = InitialValues(susceptibles=S0, infected=I0, removed=R0)
    scenario = SIRScenario(initial_conditions=initial_conditions, disease=None)
    population_evolution = scenario.compute_evolution(n_days)

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

    graph = MainGraph(population_evolution, layout)

    return graph


