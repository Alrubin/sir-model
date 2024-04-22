from unittest import TestCase
from parameterized import parameterized
from pydantic import ValidationError
from lib.disease import Disease


class DiseaseTestcase(TestCase):

    def test_on_disease_rates(self):
        disease = my_disease(0, 0, 0, 0)

        self.assertCountEqual(["tasso_di_infettività",
                               "tasso_di_contagio",
                               "virulenza",
                               "tasso_di_riinfezione"],
                              disease.rates)

    @parameterized.expand([
        (0, 0, 0, 0, False),
        (-1, 0, 0, 0, True),
        (0, -1, 0, 0, True),
        (1, 0, -1, 0, True),
        (0, 0, 0, -1, True),
        (1, 0, 0, 0, False),
        (0, 1, 0, 0, False),
        (0, 0, 1, 0, False),
        (0, 0, 0, 1, False),
        (2, 0, 0, 0, True),
        (0, 2, 0, 0, False),
        (0, 0, 2, 0, True),
        (0, 0, 0, 2, True),
    ])
    def test_raise_error_on_invalid_rates(self, tasso_di_infettività, tasso_di_contagio, virulenza,
                                          tasso_di_riinfezione, expected_to_raise_exception):
        if expected_to_raise_exception:
            with self.assertRaises(ValidationError):
                my_disease(tasso_di_infettività, tasso_di_contagio, virulenza, tasso_di_riinfezione)
        else:
            my_disease(tasso_di_infettività, tasso_di_contagio, virulenza, tasso_di_riinfezione)


def my_disease(tasso_di_infettività, tasso_di_contagio, virulenza, tasso_di_riinfezione):
    return Disease(tasso_di_infettività=tasso_di_infettività,
                   tasso_di_contagio=tasso_di_contagio,
                   virulenza=virulenza,
                   tasso_di_riinfezione=tasso_di_riinfezione
                   )
