import numpy as np
from scipy.integrate import odeint
from lib.disease import SIRDisease
from lib.model import SIRModel
from lib.population import SIRPopulationState, build_sir_population


class Scenario:
    def __init__(self, initial_conditions: SIRPopulationState, disease: SIRDisease):
        self.initial_conditions = initial_conditions
        self.disease = disease

    def compute_evolution(self, n_days):
        population_evolution = [self.initial_conditions]
        if n_days != 0:
            time_grid = np.linspace(start=0, stop=n_days, num=n_days)
            model = SIRModel(disease=self.disease)
            population_evolution += [build_sir_population(*population) for population in odeint(model, self.initial_conditions.array(), time_grid)]

        return population_evolution
