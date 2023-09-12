import unittest

class Ahorcado():
  palabra_correcta = "agiles"
  vidas = 3
  
  # Cuando la letra ingresada es correcta, retorna True.
  # Cuando la letra ingresada es incorrecta, retorna False.
  # Cuando el input es inválido, retorna False.
  def ingresa_letra(self, letra):
    if not letra.isalpha():
      return False
    
    if letra not in self.palabra_correcta:
      self.vidas = self.vidas - 1
      return False
    
    return True

  # Cuando la palabra ingresada es la correcta, retorna True.
  # Cuando la palabra ingresada es la incorrecta, retorna False.
  def ingresa_palabra(self, palabra):
    if palabra != self.palabra_correcta:
      return False
    return True

class AhorcadoTests(unittest.TestCase):

  def setUp(self):
    self.ahorcado = Ahorcado()
  
  def test_ingresa_simbolo(self):
    self.assertFalse(self.ahorcado.ingresa_letra("*"))

  def test_ingresa_letra_erronea_vidas(self):
    self.ahorcado.ingresa_letra("B")
    self.assertEqual(self.ahorcado.vidas, 2)

  def test_ingresa_letra_correcta_vidas(self):
    self.ahorcado.ingresa_letra("a")
    self.assertEqual(self.ahorcado.vidas, 3)

  def test_ingresa_letra_erronea(self):
    self.assertFalse(self.ahorcado.ingresa_letra("B"))

  def test_ingresa_letra_correcta(self):
    self.assertTrue(self.ahorcado.ingresa_letra("a"))

  def test_ingresa_palabra_erronea(self):
    self.assertFalse(self.ahorcado.ingresa_palabra("metodologias"))

  def test_ingresa_palabra_correcta(self):
    self.assertTrue(self.ahorcado.ingresa_palabra("agiles"))

if __name__ == '__main__':
    unittest.main()