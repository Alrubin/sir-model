import unittest

from lib.model import SIRModelPopulation


class SIRModelPopulationTest(unittest.TestCase):

    def test_base(self):
        distribution = SIRModelPopulation(susceptible=5, infected=10, removed=15)

        self.assertCountEqual(["susceptible", "infected", "removed"], distribution.states)
        self.assertEqual(5, distribution.susceptible)
        self.assertEqual(10, distribution.infected)
        self.assertEqual(15, distribution.removed)



