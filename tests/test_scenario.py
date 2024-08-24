import unittest
from parameterized import parameterized
from lib.disease import SIRDisease
from lib.population import InitialValues
from lib.scenario import SIRScenario


class ScenarioTest(unittest.TestCase):
    @parameterized.expand([0, 1, 10])
    def test_base(self, n):
        initial_conditions = InitialValues(susceptibles=10, infected=10, removed=10)
        disease = SIRDisease(transmission_rate=0.1, recovery_rate=0.1)
        scenario = SIRScenario(initial_conditions=initial_conditions, disease=disease)

        population_evolution = scenario.compute_evolution(n_days=n)

        self.assertEqual(len(population_evolution), n + 1)
        self.assertEqual(initial_conditions, population_evolution[0])
