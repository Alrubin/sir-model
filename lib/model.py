from typing import Union, List
from lib.disease import SIRDisease
from lib.population import SIRPopulationState


class SIRModel:
    def __init__(self, disease: Union[None, SIRDisease] = None):
        self.tr = disease.transmission_rate if disease else 0
        self.rr = disease.recovery_rate if disease else 0

    def __call__(self, y: Union[SIRPopulationState, List[float]], t: float):
        S, I, R = y.array() if isinstance(y, SIRPopulationState) else y
        dSdt = -self.tr * S * I
        dIdt = self.tr * S * I - self.rr * I
        dRdt = self.rr * I
        return dSdt, dIdt, dRdt
