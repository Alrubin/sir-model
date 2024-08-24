from typing import Union
import numpy as np
from scipy.integrate import odeint

from components.main_graph import update_graph
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

    graph = update_graph(population_evolution)

    return graph
