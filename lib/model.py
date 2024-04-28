from typing import List
from pydantic import BaseModel, NonNegativeInt
from lib.disease import Disease


class SIRModelPopulation(BaseModel):
    susceptible: NonNegativeInt
    infected: NonNegativeInt
    removed: NonNegativeInt

    @property
    def states(self) -> List[str]:
        return list(self.__dict__.keys())


class SIRModel:
    def __init__(self, disease: Disease):
        self.tr = disease.transmission_rate
        self.rr = disease.recovery_rate

    def __call__(self, y: SIRModelPopulation):
        S, I, R = y.susceptible, y.infected, y.removed
        dSdt = -self.tr * S * I
        dIdt = self.tr * S * I - self.rr * I
        dRdt = self.rr * I
        return dSdt, dIdt, dRdt
