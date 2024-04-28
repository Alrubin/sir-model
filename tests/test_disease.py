from unittest import TestCase
from lib.disease import Disease


class DiseaseTestcase(TestCase):

    def test_on_disease_rates(self):
        disease = my_disease(0.1, 0.1)

        self.assertCountEqual(["transmission_rate","recovery_rate"], disease.rates)


def my_disease(transmission_rate, recovery_rate):
    return Disease(transmission_rate=transmission_rate,
                   recovery_rate=recovery_rate
                   )
