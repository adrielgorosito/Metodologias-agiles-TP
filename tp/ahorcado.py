# Política de puntuaciones - Reglas de negocio
# Acierto de palabra entera

## Cuando no hubo letras intentadas correctas: 1000 puntos
### (cuando letras_incorrectas = 0 y estado_palabra = [_ _ _])
## Cuando hubo letras intentadas correctas: 500 puntos
### (plantear en un futuro tener en cuenta letras intentadas)

# Acierto de una letra
## La letra es correcta: 10 puntos
## La letra es incorrecta: -10 puntos



class Ahorcado:
  palabra_correcta = ""
  letras_incorrectas = []
  estado_palabra = []
  vidas = 7
  puntaje_partida = 0

  def __init__(self, palabra_correcta):
    # TODO: Al parecer hay que definir los atributos de la clase en el metodo __init__ sino
    # toman los valores de otra inicialización.
    
    self.palabra_correcta = palabra_correcta
    self.estado_palabra = []

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
    if palabra != self.palabra_correcta:
      return False

    self.puntaje_partida = 100
    return True