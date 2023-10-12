import unittest

from src.lab1.calculator import calculator


class CalculatorTestCase(unittest.TestCase):
    def test_summation(self):
        result = calculator("32 + 10")
        self.assertEquals(result, 42)
        print("Test 'summation' completed")

    def test_subtraction(self):
        result = calculator("16 - 15")
        self.assertEquals(result, 1)
        print("Test 'subtraction' completed")

    def test_multiplication(self):
        result = calculator("5 * 4")
        self.assertEquals(result, 20)
        print("Test 'multiplication' completed")

    def test_division(self):
        result = calculator("32 / 16")
        self.assertEquals(result, 2)
        print("Test 'division' completed")

    def test_division_by_zero(self):
        result = calculator("32 / 0")
        self.assertEquals(result, "Error! Incorrect expression")
        print("Test 'division_by_zero' completed")

    def test_random_bad_expression(self):
        result = calculator("qeweqweqwqwe12321()()()()")
        self.assertEquals(result, "Error! Incorrect expression")
        print("Test 'random_bad_expression' completed")

    def test_sin(self):
        result = calculator("sin(45)")
        self.assertEquals(result, 0.8509035245341184)
        print("Test 'sin' completed")

    def test_cos(self):
        result = calculator("cos(45)")
        self.assertEquals(result, 0.5253219888177297)
        print("Test 'sin' completed")

    def test_sin_radians(self):
        result = calculator("sin(radians(90))")
        self.assertEquals(result, 1.0)
        print("Test 'sin_radians' completed")

    def test_pow(self):
        result = calculator("pow(10, 2)")
        self.assertEquals(result, 100.0)
        print("Test 'pow' completed")


if __name__ == "__main__":
    unittest.main()
