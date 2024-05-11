from pydantic import BaseModel, NonNegativeFloat
from typing import NamedTuple


class Susceptibles(BaseModel):
    value: NonNegativeFloat


class Infected(BaseModel):
    value: NonNegativeFloat


class Removed(BaseModel):
    value: NonNegativeFloat


class SIRPopulationState(NamedTuple):
    susceptibles: Susceptibles
    infected: Infected
    removed: Removed

    def array(self):
        return [self.susceptibles.value, self.infected.value, self.removed.value]


def build_sir_population(susceptibles, infected, removed):
    return SIRPopulationState(susceptibles=Susceptibles(value=susceptibles),
                              infected=Infected(value=infected),
                              removed=Removed(value=removed)
                              )
