import unittest

class Calc():
  def sum(self, int1, int2):
    return int1 + int2

class CalcTest(unittest.TestCase):

  def test_args_cero_rta_cero(self):
    
    calculadora = Calc()

    self.assertEqual(calculadora.sum(0, 0), 0)

  def test_args_dos_rta_cuatro(self):
    
    calculadora = Calc()

    self.assertEqual(calculadora.sum(2, 2), 4)

  def test_args_dos_tres_rta_cinco(self):
    
    calculadora = Calc()

    self.assertEqual(calculadora.sum(2, 3), 5)

if __name__ == '__main__':
    unittest.main()