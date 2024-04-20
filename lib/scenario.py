from pydantic import BaseModel, NonNegativeInt


class Scenario(BaseModel):
    population: NonNegativeInt
