"""Tests for the command-line interface (simulated user input)."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from src import interface

#todas estas herramientas son para simular la entrada de datos y la salida de datos en la consola, para poder probar el menu sin tener que escribir manualmente cada vez.
#io, redirect_stdout, crean una PANTALLA INVIISBLE, no se llega a imprimir ls cosas si no q se quedan guardadas para ser leidas posteriormente
#patch(unittest.mock) reemplaza la funcion de input por respuestas PREGRABADAS
#
def run_with_inputs(inputs):
    """Run the menu feeding `inputs` as typed text; return printed output."""
    buffer = io.StringIO()
    with patch("builtins.input", side_effect=inputs), redirect_stdout(buffer):
        interface.main_menu()
    return buffer.getvalue()


class TestINTERFACE(unittest.TestCase):
    """End-to-end tests of the menu."""

    def test_exit(self):
        self.assertIn("Goodbye!", run_with_inputs(["0"]))

    def test_bmi_flow(self):
        out = run_with_inputs(["1", "70", "175", "0"])
        self.assertIn("22.9", out)
        self.assertIn("Normal weight", out)

    def test_heart_zone_flow(self):
        out = run_with_inputs(["2", "30", "140", "0"])
        self.assertIn("Zone 3", out)

    def test_calories_flow(self):
        out = run_with_inputs(["3", "m", "70", "175", "30", "3","maintain", "0"])
        self.assertIn("2556 kcal", out)

    def test_water_flow(self):
        out = run_with_inputs(["4", "70", "60", "0"])
        self.assertIn("2950 ml", out)

    def test_invalid_menu_option_is_retried(self):
        out = run_with_inputs(["9", "0"])
        self.assertIn("Invalid option", out)

    def test_invalid_number_is_retried(self):
        out = run_with_inputs(["1", "abc", "70", "175", "0"])
        self.assertIn("Invalid number", out)

    def test_out_of_range_is_retried(self):
        out = run_with_inputs(["1", "500", "70", "175", "0"])
        self.assertIn("must be between", out)
        
    def test_heart_rate_above_max_shows_error(self):
        out = run_with_inputs(["2", "30", "190", "0"])
        self.assertIn("Error", out)

if __name__ == "__main__":
    unittest.main()


    """"lo q hace este codigo de test es que como se usa el input() en el MENU
    y print() para mostrar y probar como si hubiera una ejecucion humana de por medio
    es deci comprueba si la consola del menu funciona correctamente
    """