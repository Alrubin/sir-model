from typing import List

from pydantic import BaseModel, NonNegativeInt

class SIRModelPopulation(BaseModel):
    susceptible: NonNegativeInt
    infected: NonNegativeInt
    removed: NonNegativeInt

    @property
    def states(self) -> List[str]:
        return list(self.__dict__.keys())

