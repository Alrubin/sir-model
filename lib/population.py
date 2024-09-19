from pydantic import NonNegativeInt, model_validator, BaseModel
from typing import NamedTuple


class Population(NamedTuple):
    susceptibles: float
    infected: float
    removed: float


class InitialValues(BaseModel):
    population: NonNegativeInt
    infected: NonNegativeInt
    removed: NonNegativeInt

    @property
    def susceptibles(self):
        return self.population - self.infected - self.removed

    def array(self):
        return Population(
            susceptibles=self.susceptibles,
            infected=self.infected,
            removed=self.removed
        )

    @model_validator(mode='after')
    def check_population(cls, values):
        if values.population - values.infected - values.removed < 0:
            raise ValueError("Initial susceptibles cannot be negative.")
        return values



