class InvalidPopulationError(ValueError):
    pass


class Scenario:
    def __init__(self, population):
        self.validate_population_attribute(population)
        self.population = population

    def validate_population_attribute(self, population):
        if not isinstance(population, int):
            raise InvalidPopulationError("The population parameter must be an integer")
        if population < 0:
            raise InvalidPopulationError("The population parameter must be greater or equal than 0")
