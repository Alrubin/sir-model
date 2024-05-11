from unittest import TestCase
from parameterized import parameterized
from lib.disease import SIRDisease


class SIRDiseaseTest(TestCase):

    @parameterized.expand([
        (0.2, 5),
        (0.1, 10),
        (1, 1)
    ])
    def test_on_mean_duration_of_infection(self, recovery_rate, expected_mean_duration):
        disease = SIRDisease(transmission_rate=0.1,
                             recovery_rate=recovery_rate
                             )

        mean_duration = disease.mean_duration()

        self.assertEqual(expected_mean_duration, mean_duration)
