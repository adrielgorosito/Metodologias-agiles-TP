Feature: Verificar funcionalidades de la aplicación web

  Background:
    Given requerimientos

  Scenario: Iniciar partida
    Given ingreso la palabra "elefante"
    Then debería ver la palabra con la misma cantidad de guiones bajos que letras

  Scenario: Ingresar letra válida
    Given ingreso la palabra "elefante"
    When intento la letra correcta "e"
    Then debería ver la letra revelada en la palabra