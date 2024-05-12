import unittest
from lib.disease import SIRDisease
from lib.population import build_sir_population
from lib.model import SIRModel


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


class SIRModelTest(unittest.TestCase):
    def test_base(self):
        initial_conditions = build_sir_population(10, 10, 10)
        disease = SIRDisease(transmission_rate=0.1, recovery_rate=0.1)
        model = SIRModel(disease=disease)

        gradient = model(initial_conditions, 0)

        self.assertEqual((-10.0, 9.0, 1.0), gradient)

    def test_absence_of_disease(self):
        population = build_sir_population(10, 10, 10)
        model = SIRModel(disease=None)

        gradient = model(population, 0)

        self.assertEqual((0.0, 0.0, 0.0), gradient)

    def test_compatibility_with_list_of_floats(self):
        population = [10, 10, 10]
        model = SIRModel(disease=None)

        gradient = model(population, 0)

        self.assertEqual((0.0, 0.0, 0.0), gradient)
