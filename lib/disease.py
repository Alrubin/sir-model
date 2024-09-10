from pydantic import BaseModel, PositiveFloat


class SIRDisease(BaseModel):
    transmission_rate: PositiveFloat
    recovery_rate: PositiveFloat

    def mean_duration(self):
        return 1 / self.recovery_rate

def build_disease(transmission_rate, recovery_rate):
    if transmission_rate == 0 and recovery_rate == 0:
        return None
    return SIRDisease(transmission_rate=transmission_rate, recovery_rate=recovery_rate)