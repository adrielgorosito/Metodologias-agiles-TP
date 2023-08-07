import unittest

class Calc():
  def sum(self, int1, int2):
    return int1 + int2

class CalcTest(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calc()

    def test_sum_of_two_zeros_returns_zero(self):
        self.assertEqual(self.calculadora.sum(0, 0), 0)

    def test_sum_two_and_two_returns_four(self):
        self.assertEqual(self.calculadora.sum(2, 2), 4)

    def test_sum_two_and_three_returns_five(self):
        self.assertEqual(self.calculadora.sum(2, 3), 5)

    def test_sum_negative_numbers_returns_correct_result(self):
        self.assertEqual(self.calculadora.sum(-2, -3), -5)

    def test_sum_large_numbers_returns_correct_result(self):
        self.assertEqual(self.calculadora.sum(1000000, 2000000), 3000000)

if __name__ == '__main__':
    unittest.main()