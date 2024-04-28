import unittest
from lib.disease import Disease
from lib.model import Population
from lib.model import SIRModel


class PopulationTest(unittest.TestCase):

    def test_base(self):
        distribution = Population(susceptible=5, infected=10, removed=15)

        self.assertEqual(5, distribution.susceptible)
        self.assertEqual(10, distribution.infected)
        self.assertEqual(15, distribution.removed)


class SIRModelTest(unittest.TestCase):
    def test_base(self):
        initial_conditions = Population(susceptible=10, infected=10, removed=10)
        disease = Disease(transmission_rate=0.1, recovery_rate=0.1)
        model = SIRModel(disease=disease)

        gradient = model(initial_conditions)

        self.assertEqual((-10.0, 9.0, 1.0), gradient)

    def test_absence_of_disease(self):
        population = Population(susceptible=10, infected=10, removed=10)
        model = SIRModel(disease=None)

        gradient = model(population)

        self.assertEqual((0.0, 0.0, 0.0), gradient)