from pydantic import BaseModel, confloat, NonNegativeFloat
from typing import List

FloatBetweenZeroAndOne = confloat(ge=0.0, le=1.0)

class Disease(BaseModel):
    tasso_di_contagio: NonNegativeFloat
    tasso_di_infettività: FloatBetweenZeroAndOne
    virulenza: FloatBetweenZeroAndOne
    tasso_di_riinfezione: FloatBetweenZeroAndOne

    @property
    def rates(self) -> List[str]:
        return list(self.__dict__.keys())

