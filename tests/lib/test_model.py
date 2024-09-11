import unittest
from lib.disease import SIRDisease
from lib.population import InitialValues
from lib.model import SIRModel


class SIRModelTest(unittest.TestCase):
    def test_base(self):
        initial_conditions = InitialValues(population=100, infected=10, removed=10)
        disease = SIRDisease(transmission_rate=0.1, recovery_rate=0.1)
        model = SIRModel(disease=disease)

        gradient = model(initial_conditions.array(), 0)

        self.assertEqual(gradient, (-80.0, 79.0, 1.0))

    def test_absence_of_disease(self):
        initial_conditions = InitialValues(population=100, infected=10, removed=10)
        model = SIRModel(disease=None)

        gradient = model(initial_conditions.array(), 0)

        self.assertEqual(gradient, (0.0, 0.0, 0.0))

    def test_compatibility_with_list_of_floats(self):
        population = [10, 10, 10]
        model = SIRModel(disease=None)

        gradient = model(population, 0)

        self.assertEqual(gradient, (0.0, 0.0, 0.0))
