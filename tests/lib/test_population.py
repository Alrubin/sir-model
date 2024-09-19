import unittest

from parameterized import parameterized

from lib.population import InitialValues


class TestInitialValues(unittest.TestCase):

    @parameterized.expand([
        (20, 10, 70, 20, 10),
        (50, 50, 0, 50, 50)

    ])
    def test_valid_initial_values(self, infected, removed, expected_susceptibles, expected_infected, expected_removed):
        initial_values = InitialValues(population=100, infected=infected, removed=removed)

        array = initial_values.array()

        self.assertEqual(array.susceptibles, expected_susceptibles)
        self.assertEqual(array.infected, expected_infected)
        self.assertEqual(array.removed, expected_removed)

    def test_population_less_than_infected_and_removed(self):
        with self.assertRaises(ValueError):
            InitialValues(population=25, infected=15, removed=20)
