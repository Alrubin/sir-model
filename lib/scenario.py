from typing import Union

import numpy as np
from dash import dcc
from scipy.integrate import odeint

from components.main_graph import ScatterLine, MainGraph, layout
from lib.disease import SIRDisease
from lib.model import SIRModel
from lib.population import InitialValues, Population


class SIRScenario:
    def __init__(self, initial_conditions: InitialValues, disease: Union[None, SIRDisease] = None):
        self.initial_conditions = initial_conditions
        self.disease = disease
        self._model = SIRModel(disease=self.disease)

    def update_graph(self, n_days):
        population_evolution = self.compute_evolution(n_days)

        susceptibles = [population.susceptibles for population in population_evolution]
        infected = [population.infected for population in population_evolution]
        removed =[population.removed for population in population_evolution]
        giorni = list(range(n_days + 1))

        fig = MainGraph([
            ScatterLine(giorni, susceptibles, 'Suscettibili', 'royalblue'),
            ScatterLine(giorni, infected, 'Infetti', 'red'),
            ScatterLine(giorni, removed, 'Rimossi', 'green')
        ],
            layout
        )

        return dcc.Graph(figure=fig)

    def compute_evolution(self, n_days) -> list[Population]:
        initial_conditions = np.array(self.initial_conditions).reshape(1, -1)
        time_grid = np.linspace(start=0, stop=n_days, num=n_days)
        population_evolution = odeint(self._model, self.initial_conditions, time_grid)

        return [Population(*population) for population in np.vstack((initial_conditions, population_evolution))]


def update_scenario(S0, I0, R0, n_days):
    initial_conditions = InitialValues(susceptibles=S0, infected=I0, removed=R0)

    scenario = SIRScenario(initial_conditions=initial_conditions, disease=None)

    graph = scenario.update_graph(n_days)

    return graph
