"""Unit tests for src/calculator.py."""

import unittest

from src import calculator as calc


class TestBMI(unittest.TestCase):
    """Tests for BMI calculation and classification."""

    def test_normal_bmi(self):
        self.assertEqual(calc.calculate_bmi(70, 175), 22.9) #ese 22.9 es lo q deberia dar segun la formula del bmi redondeada para 175cm y 70kg

    def test_invalid_values(self): # si metes peso de 0 o altura negativa da error
        with self.assertRaises(ValueError):
            calc.calculate_bmi(0, 175) #caso de peso NO VALIDO
        with self.assertRaises(ValueError):
            calc.calculate_bmi(70, -1) #CASO ALTURA NO VALIDA
#verifica que si tu funcion da x se devuelva el resultado correcto, si no es asi, da error y nos dice que la funcion no funciona correctamente.
    def test_categories(self): 
        self.assertEqual(calc.classify_bmi(17.0), "Underweight")
        self.assertEqual(calc.classify_bmi(18.5), "Normal weight")
        self.assertEqual(calc.classify_bmi(24.9), "Normal weight")
        self.assertEqual(calc.classify_bmi(27.0), "Overweight")
        self.assertEqual(calc.classify_bmi(30.0), "Obesity")


class TestHeartRate(unittest.TestCase):
    """Tests for maximum heart rate and training zones."""

    def test_max_heart_rate(self):
        self.assertEqual(calc.max_heart_rate(30), 187) #para 30 años el pulso es 187 por ej

    def test_zone_boundaries(self):
        # Age 30 -> max 187 bpm
        # Cambiado get_heart_rate_zone -> heart_rate_zone
        self.assertEqual(calc.heart_rate_zone(30, 80)[0], 0) #prueba para 30 años que se cumplen todos los rangos
        self.assertEqual(calc.heart_rate_zone(30, 100)[0], 1)
        self.assertEqual(calc.heart_rate_zone(30, 120)[0], 2)
        self.assertEqual(calc.heart_rate_zone(30, 140)[0], 3)
        self.assertEqual(calc.heart_rate_zone(30, 160)[0], 4)
        self.assertEqual(calc.heart_rate_zone(30, 187)[0], 5)
#si a=b ok si a=!b error,la funcion no develve lo q deberia de devolver
 
    def test_percent_returned(self):
        self.assertEqual(calc.heart_rate_zone(30, 140)[2], 74.9)

    def test_invalid(self): #valuerror si las pulsaciones o edad son 0 o values no posibles
        with self.assertRaises(ValueError):
            calc.heart_rate_zone(30, -1)
        with self.assertRaises(ValueError):
            calc.heart_rate_zone(30, 200)
        with self.assertRaises(ValueError):
            calc.max_heart_rate(0)


class TestCalories(unittest.TestCase):
    """Tests for BMR and daily calories."""

    def test_bmr_male(self):
        self.assertAlmostEqual(calc.calculate_bmr("male", 70, 175, 30),1648.75, places=2)

    def test_bmr_female(self):
        self.assertAlmostEqual(calc.calculate_bmr("female", 70, 175, 30),1482.75, places=2)

    def test_calories_by_goal(self):
        # Cambiado 3 por el multiplicador real 1.55 (actividad moderada)
        args = ("male", 70, 175, 30, 3) #args es tupla de 5 datos fijos de una persona para comprobar en el test
        self.assertEqual(calc.calculate_daily_calories(*args, "maintain"),
                         2556)
        self.assertEqual(calc.calculate_daily_calories(*args, "lose"), 2056)
        self.assertEqual(calc.calculate_daily_calories(*args, "gain"), 2856)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calc.calculate_bmr("other", 70, 175, 30)
        
        with self.assertRaises(ValueError):
            calc.calculate_daily_calories("male", 70, 175, 30, 9, "lose")
        with self.assertRaises(ValueError):
            calc.calculate_daily_calories("male", 70, 175, 30, 3, "fly")


class TestWater(unittest.TestCase):
    """Tests for daily water calculation."""

    def test_no_exercise(self):
        self.assertEqual(calc.calculate_daily_water(70, 0), 2450)

    def test_with_exercise(self):
        self.assertEqual(calc.calculate_daily_water(70, 60), 2950)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            calc.calculate_daily_water(-5, 10)
        with self.assertRaises(ValueError):
            calc.calculate_daily_water(70, -10)


if __name__ == "__main__":
    unittest.main()

"""lo q hacemos aqui es comprobar automaticamente si las funciones que tenemos en la calculadora son correctss o tieenen algun error
lo hacemos mediante pruebas unitarias, es decir, pruebas que se hacen a cada funcion de manera individual para ver si funciona correctamente.
en vez de comprobar todo metiendo datos manualmente, lo hacemos automaticamente y nos devuelve un resultado de si la funcion funciona correctamente o no.
"""