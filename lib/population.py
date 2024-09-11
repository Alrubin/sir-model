from pydantic import NonNegativeInt
from typing import NamedTuple


class InitialValues(NamedTuple):
    population: NonNegativeInt
    infected: NonNegativeInt
    removed: NonNegativeInt

    @property
    def susceptibles(self):
        return self.population - self.infected - self.removed

    def array(self):
        return [self.susceptibles, self.infected, self.removed]


class Population(NamedTuple):
    susceptibles: float
    infected: float
    removed: float
