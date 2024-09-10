import unittest
from unittest import TestCase
from parameterized import parameterized
from lib.disease import SIRDisease, build_disease


class SIRDiseaseTest(TestCase):

    @parameterized.expand([
        (0.2, 5),
        (0.1, 10),
        (1, 1)
    ])
    def test_on_mean_duration_of_infection(self, recovery_rate, expected_mean_duration):
        disease = SIRDisease(transmission_rate=0.1, recovery_rate=recovery_rate)

        mean_duration = disease.mean_duration()

        self.assertEqual(expected_mean_duration, mean_duration)


class TestDiseaseBuilder(unittest.TestCase):
    def test_build_disease_gives_none_when_trivial_params(self):
        transmission_rate = 0
        recovery_rate = 0

        disease = build_disease(transmission_rate, recovery_rate)

        self.assertEqual(disease, None)

    def test_build_disease_base_case(self):
        transmission_rate = 0.1
        recovery_rate = 0.1

        disease = build_disease(transmission_rate, recovery_rate)

        self.assertIsInstance(disease, SIRDisease)
        self.assertEqual(disease.transmission_rate, 0.1)
        self.assertEqual(disease.recovery_rate, 0.1)
