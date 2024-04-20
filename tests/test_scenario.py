from unittest import TestCase
from parameterized import parameterized
from lib.scenario import Scenario
from pydantic import ValidationError


class ScenarioTestCase(TestCase):

    @parameterized.expand([
        (2, False),
        (0, False),
        (-2, True)
    ])
    def test_raise_error_on_negative_population(self, population, expected_to_raise_exception):
        if expected_to_raise_exception:
            with self.assertRaises(ValidationError):
                Scenario(population=population)
        else:
            Scenario(population=population)

    @parameterized.expand([
        (2, False),
        (2.0, False),
        (2.1, True),
        ("2", False),
        ("2.1", True),
        (None, True)
    ])
    def test_raise_when_population_is_not_an_integer(self, population, expected_to_raise_exception):
        if expected_to_raise_exception:
            with self.assertRaises(ValidationError):
                Scenario(population=population)
        else:
            Scenario(population=population)
