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
