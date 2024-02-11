Feature: Verificar funcionalidades del ahorcado

  Background:
    Given requerimientos

  Scenario: Iniciar partida
    Given ingreso la palabra "elefante"
    Then debería ver la palabra con la misma cantidad de guiones bajos que letras

  Scenario: Ingresar letra válida
    Given ingreso la palabra "elefante"
    When intento la letra "e"
    Then debería ver la letra revelada en la palabra
    Then la cantidad de vidas debería ser "7"

  Scenario: Ingresar letra inválida
    Given ingreso la palabra "elefante"
    When intento la letra "x"
    Then debería ver la letra en la letras incorrectas
    Then la cantidad de vidas debería ser "6"

  Scenario: Arriesgo la palabra correcta
    Given ingreso la palabra "elefante"
    When arriesgo la palabra "elefante"
    Then debería aparecerme un cartel que diga "Ganaste!"

  Scenario: Arriesgo una palabra incorrecta
    Given ingreso la palabra "elefante"
    When arriesgo la palabra "dinosaurio"
    Then debería aparecerme un cartel que diga "Perdiste!"