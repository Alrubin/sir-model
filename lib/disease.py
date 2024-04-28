from pydantic import BaseModel, PositiveFloat
from typing import List

class Disease(BaseModel):
    transmission_rate: PositiveFloat
    recovery_rate: PositiveFloat

    @property
    def rates(self) -> List[str]:
        return list(self.__dict__.keys())

