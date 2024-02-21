class Ahorcado:
  palabra_correcta = ""
  letras_incorrectas = []
  estado_palabra = []
  vidas = 7

  def __init__(self, palabra_correcta):
    self.palabra_correcta = palabra_correcta
    self.estado_palabra = []
    self.letras_incorrectas = []
    self.vidas = 7

    for _ in palabra_correcta:
      self.estado_palabra.append("_")
  
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
    self.vidas = 0
    
    if palabra != self.palabra_correcta:
      return False
    return True
