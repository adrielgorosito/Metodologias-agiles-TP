import unittest
from ahorcado import Ahorcado
from usuario import Usuario

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

  def test_checkea_letras_incorrectas(self):
    self.ahorcado.ingresa_letra("e")
    self.ahorcado.ingresa_letra("u")
    self.ahorcado.ingresa_letra("m")

    self.assertEqual(self.ahorcado.letras_incorrectas, ["e", "u", "m"])

  def test_devuelve_estado_palabra(self):
    self.ahorcado.ingresa_letra("o")
    self.ahorcado.ingresa_letra("r")
    self.ahorcado.ingresa_letra("a")
    
    self.assertEqual(self.ahorcado.estado_palabra, ['o', '_', 'o', 'r', 'r', '_', '_', 'o', '_', 'a', 'r', '_', '_', '_', 'o', '_', 'o', '_', '_', 'a'])

  def test_aumenta_puntaje(self):
    self.ahorcado.ingresa_palabra("otorrinolaringologia")
    self.assertEqual(self.ahorcado.puntaje_partida, 100)


class UsuarioTests(unittest.TestCase):
  
  def setUp(self):
    self.usuario = Usuario()

  def test_cantidad_partidas_inicial(self):
    self.assertEqual(self.usuario.cantidad_partidas_jugadas, 0)
  
  def test_cantidad_partidas_unico_juego(self):
    self.usuario.jugar_partida()
    self.assertEqual(self.usuario.cantidad_partidas_jugadas, 1)

if __name__ == '__main__':
    unittest.main()