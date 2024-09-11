import unittest
import numpy as np
from lib.disease import SIRDisease
from lib.population import InitialValues, Population
from lib.scenario import SIRScenario
from unittest.mock import patch


class ScenarioTest(unittest.TestCase):
    @patch('lib.scenario.odeint')
    def test_base(self, mocked_odeint):
        mocked_odeint.return_value = np.array([
            [0.9, 0.1, 0.0],
            [0.8, 0.2, 0.0]
        ])
        initial_conditions = InitialValues(population=100, infected=10, removed=10)
        disease = SIRDisease(transmission_rate=0.1, recovery_rate=0.1)
        scenario = SIRScenario(initial_conditions=initial_conditions, disease=disease)

        population_evolution = scenario.compute_evolution(n_days=1)

        mocked_odeint.assert_called()
        self.assertEqual(population_evolution, [
            Population(susceptibles=80.0, infected=10.0, removed=10.0),
            Population(susceptibles=0.9, infected=0.1, removed=0.0),
            Population(susceptibles=0.8, infected=0.2, removed=0.0)
        ])
