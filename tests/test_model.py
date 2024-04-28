import unittest

from parameterized import parameterized

from lib.disease import Disease
from lib.model import Population, Scenario
from lib.model import SIRModel


class PopulationTest(unittest.TestCase):

    def test_base(self):
        population = Population(susceptible=5, infected=10, removed=15).tuple()

        self.assertEqual((5, 10, 15), population)


class SIRModelTest(unittest.TestCase):
    def test_base(self):
        initial_conditions = Population(susceptible=10, infected=10, removed=10).tuple()
        disease = Disease(transmission_rate=0.1, recovery_rate=0.1)
        model = SIRModel(disease=disease)

        gradient = model(initial_conditions, 0)

        self.assertEqual((-10.0, 9.0, 1.0), gradient)

    def test_absence_of_disease(self):
        population = Population(susceptible=10, infected=10, removed=10).tuple()
        model = SIRModel(disease=None)

        gradient = model(population, 0)

        self.assertEqual((0.0, 0.0, 0.0), gradient)


class ScenarioTest(unittest.TestCase):
    @parameterized.expand([0, 1, 10])
    def test_base(self, n):
        initial_conditions = Population(susceptible=10, infected=10, removed=10)
        disease = Disease(transmission_rate=0.1, recovery_rate=0.1)

        scenario = Scenario(initial_conditions=initial_conditions, disease=disease)
        susceptible_evolution, infected_evolution, removed_evolution = scenario.build(n_days=n)

        self.assertEqual(len(susceptible_evolution), n)
        self.assertEqual(len(infected_evolution), n)
        self.assertEqual(len(removed_evolution), n)
