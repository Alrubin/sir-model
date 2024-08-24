from pydantic import NonNegativeInt
from typing import NamedTuple


class InitialValues(NamedTuple):
    susceptibles: NonNegativeInt
    infected: NonNegativeInt
    removed: NonNegativeInt

class Population(NamedTuple):
    susceptibles: float
    infected: float
    removed: float

