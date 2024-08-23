from typing import Union

import numpy as np
from scipy.integrate import odeint

from config import GraphLayoutSettings
from components.main_graph import ScatterLine, MainGraph
from lib.disease import SIRDisease
from lib.model import SIRModel
from lib.population import InitialValues
import pandas as pd


class Scenario:
    def __init__(self, initial_conditions: InitialValues, disease: Union[None, SIRDisease] = None):
        self.initial_conditions = initial_conditions
        self.disease = disease
        self._model = SIRModel(disease=self.disease)

    def update_graph(self, n_days):
        population_evolution = self.compute_evolution(n_days)

        df = pd.DataFrame(population_evolution, columns=["S", "I", "R"])
        df["Giorno"] = range(n_days + 1)

        graph = MainGraph([
            ScatterLine(df['Giorno'], df['S'], 'Suscettibili', 'royalblue'),
            ScatterLine(df['Giorno'], df['I'], 'Infetti', 'red'),
            ScatterLine(df['Giorno'], df['R'], 'Rimossi', 'green')
        ],
            GraphLayoutSettings()
        ).build()

        return graph

    def compute_evolution(self, n_days):
        population_evolution = [self.initial_conditions]
        if n_days != 0:
            time_grid = np.linspace(start=0, stop=n_days, num=n_days)
            population_evolution += [pop for pop in odeint(self._model, self.initial_conditions, time_grid)]

        return population_evolution


def update_scenario(S0, I0, R0, n_days):
    initial_conditions = InitialValues(susceptibles=S0, infected=I0, removed=R0)

    scenario = Scenario(initial_conditions=initial_conditions, disease=None)

    graph = scenario.update_graph(n_days)

    return graph
