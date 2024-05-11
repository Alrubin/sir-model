from pydantic import BaseModel, PositiveFloat

class Disease(BaseModel):
    transmission_rate: PositiveFloat
    recovery_rate: PositiveFloat

    def mean_duration(self):
        return 1/self.recovery_rate

