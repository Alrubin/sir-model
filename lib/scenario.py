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
        if n_days == 0:
            return [self.initial_conditions]
        else:
            time_grid = np.linspace(start=0, stop=n_days, num=n_days)
            model = SIRModel(disease=self.disease)
            def model_fn(y, t):
                S, I, R = y
                population = build_sir_population(S, I, R)
                gradient = model(population, t)
                return gradient

            population_evolution = odeint(model_fn, self.initial_conditions.array(), time_grid)
            return [self.initial_conditions] + [build_sir_population(*population) for population in population_evolution]
