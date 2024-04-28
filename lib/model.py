from typing import Union
from pydantic import BaseModel, NonNegativeInt
from lib.disease import Disease


class Population(BaseModel):
    susceptible: NonNegativeInt
    infected: NonNegativeInt
    removed: NonNegativeInt

    def tuple(self):
        return self.susceptible, self.infected, self.removed


class SIRModel:
    def __init__(self, disease: Union[None, Disease] = None):
        self.tr = disease.transmission_rate if disease else 0
        self.rr = disease.recovery_rate if disease else 0

    def __call__(self, y: Population):
        S, I, R = y.susceptible, y.infected, y.removed
        dSdt = -self.tr * S * I
        dIdt = self.tr * S * I - self.rr * I
        dRdt = self.rr * I
        return dSdt, dIdt, dRdt
