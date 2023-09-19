import unittest

class Ahorcado:
  palabra_correcta = ""
  letras_incorrectas = []
  estado_palabra = []
  vidas = 7

  def __init__(self, palabra_correcta):
    Ahorcado.palabra_correcta = palabra_correcta
    for _ in palabra_correcta:
      Ahorcado.estado_palabra.append("_")
  
  # Cuando la letra ingresada es correcta, retorna el lugar que ocupa en la palabra.
  # Cuando la letra ingresada es incorrecta, retorna False.
  # Cuando el input es inválido, retorna False.
  def ingresa_letra(self, letra):
    indices_letra = []

    if not letra.isalpha():
      return False
    
    if letra not in self.palabra_correcta:
      self.vidas = self.vidas - 1
      self.letras_incorrectas.append(letra)
      return False
    
    for i, letra_palabra in enumerate(self.palabra_correcta):
      if letra_palabra == letra:
        indices_letra.append(i+1)
        self.estado_palabra[i] = letra_palabra
    
    return indices_letra

  # Cuando la palabra ingresada es la correcta, retorna True.
  # Cuando la palabra ingresada es la incorrecta, retorna False.
  def ingresa_palabra(self, palabra):
    if palabra != self.palabra_correcta:
      return False
    return True

class AhorcadoTests(unittest.TestCase):

  def setUp(self):
    self.ahorcado = Ahorcado('otorrinolaringologia')
  
  def test_ingresa_simbolo(self):
    self.assertFalse(self.ahorcado.ingresa_letra("*"))

  def test_ingresa_letra_erronea_vidas(self):
    self.ahorcado.ingresa_letra("B")
    self.assertEqual(self.ahorcado.vidas, 6)

  def test_ingresa_letra_correcta_vidas(self):
    self.ahorcado.ingresa_letra("a")
    self.assertEqual(self.ahorcado.vidas, 7)

  def test_ingresa_letra_erronea(self):
    self.assertFalse(self.ahorcado.ingresa_letra("B"))

  def test_ingresa_palabra_erronea(self):
    self.assertFalse(self.ahorcado.ingresa_palabra("metodologias"))

  def test_ingresa_palabra_correcta(self):
    self.assertTrue(self.ahorcado.ingresa_palabra("otorrinolaringologia"))

  def test_devuelve_posiciones_letra_correcta(self):
    self.assertEqual(self.ahorcado.ingresa_letra("t"), [2])

  def test_devuelve_posiciones_multiples_letra_correcta(self):
    self.assertEqual(self.ahorcado.ingresa_letra("o"), [1, 3, 8, 15, 17])

  def test_eastado_letras_incorrectas(self):
    self.ahorcado.ingresa_letra("e")
    self.ahorcado.ingresa_letra("u")
    self.ahorcado.ingresa_letra("m")

    self.assertEqual(self.ahorcado.letras_incorrectas, ["e", "u", "m"])

  def test_devuelve_estado_palabra(self):
    self.ahorcado.ingresa_letra("o")
    self.ahorcado.ingresa_letra("r")
    self.ahorcado.ingresa_letra("a")
    
    self.assertEqual(self.ahorcado.estado_palabra, ['o', '_', 'o', 'r', 'r', '_', '_', 'o', '_', 'a', 'r', '_', '_', '_', 'o', '_', 'o', '_', '_', 'a'])
    
if __name__ == '__main__':
    unittest.main()