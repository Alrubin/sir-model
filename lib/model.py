from typing import Union, Tuple

import numpy as np
from pydantic import BaseModel, NonNegativeInt
from scipy.integrate import odeint

from lib.disease import Disease


class Population(BaseModel):
    susceptible: NonNegativeInt
    infected: NonNegativeInt
    removed: NonNegativeInt

    def tuple(self):
        return self.susceptible, self.infected, self.removed


class SIRModel:
    def __init__(self, disease: Union[None, SIRDisease] = None):
        self.tr = disease.transmission_rate if disease else 0
        self.rr = disease.recovery_rate if disease else 0

    def __call__(self, y: Tuple[float], t: float):
        S, I, R = y
        dSdt = -self.tr * S * I
        dIdt = self.tr * S * I - self.rr * I
        dRdt = self.rr * I
        return dSdt, dIdt, dRdt


class Scenario:
    def __init__(self, initial_conditions: Population, disease: Disease):
        self.initial_conditions = initial_conditions
        self.disease = disease

    def build(self, n_days):
        time_grid = np.linspace(start=0, stop=n_days, num=n_days)
        model = SIRModel(disease=self.disease)
        y_evolution = odeint(model, self.initial_conditions.tuple(), time_grid)
        susceptible_evolution, infected_evolution, removed_evolution = y_evolution.T
        return susceptible_evolution, infected_evolution, removed_evolution
