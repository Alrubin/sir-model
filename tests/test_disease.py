from unittest import TestCase

from parameterized import parameterized

from lib.disease import Disease


class DiseaseTest(TestCase):

    def test_base(self):
        disease = my_disease(0.1, 0.1)

        self.assertCountEqual(["transmission_rate","recovery_rate"], disease.rates)
    @parameterized.expand([
        (0.2, 5),
        (0.1, 10),
        (1,1)
    ])
    def test_on_mean_duration_of_infection(self, recovery_rate, expected_mean_duration):
        disease = my_disease(0.1, recovery_rate)

        mean_duration = disease.mean_duration()

        self.assertEqual(expected_mean_duration, mean_duration)

def my_disease(transmission_rate, recovery_rate):
    return Disease(transmission_rate=transmission_rate,
                   recovery_rate=recovery_rate
                   )
