import unittest

from lib.population import build_sir_population


class PopulationStateTest(unittest.TestCase):

    def test_base(self):
        population = build_sir_population(5, 10, 15)

        self.assertEqual(5, population.susceptibles.value)
        self.assertEqual(10, population.infected.value)
        self.assertEqual(15, population.removed.value)

    def test_conversion_as_array(self):
        population = build_sir_population(5, 10, 15)

        population_array = population.array()

        self.assertEqual([5, 10, 15], population_array)
