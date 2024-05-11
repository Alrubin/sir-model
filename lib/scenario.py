import numpy as np
from scipy.integrate import odeint
from lib.disease import SIRDisease
from lib.model import SIRModel
from lib.population import SIRPopulationState


class Scenario:
    def __init__(self, initial_conditions: SIRPopulationState, disease: SIRDisease):
        self.initial_conditions = initial_conditions
        self.disease = disease

    def build(self, n_days):
        time_grid = np.linspace(start=0, stop=n_days, num=n_days)
        model = SIRModel(disease=self.disease)
        y_evolution = odeint(model, self.initial_conditions.array(), time_grid)
        return [self.initial_conditions]*n_days
