from unittest import TestCase
from parameterized import parameterized
from lib.scenario import Scenario, InvalidPopulationError


class ScenarioTestCase(TestCase):

    @parameterized.expand([
        (2, False),
        (0, False),
        (-2, True)
    ])
    def test_raise_error_on_negative_population(self, population, expected_to_raise_exception):
        if expected_to_raise_exception:
            with self.assertRaises(InvalidPopulationError) as context:
                Scenario(population)

            self.assertEquals("The population parameter must be greater or equal than 0", str(context.exception))
        else:
            Scenario(population)

    @parameterized.expand([
        (2, False),
        (2.0, True),
        (2.1, True)
    ])
    def test_raise_when_population_is_not_an_integer(self, population, expected_to_raise_exception):
        if expected_to_raise_exception:
            with self.assertRaises(InvalidPopulationError) as context:
                Scenario(population)

            self.assertEquals("The population parameter must be an integer", str(context.exception))
        else:
            Scenario(population)
