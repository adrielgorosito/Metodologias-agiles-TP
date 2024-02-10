Feature: Verificar funcionalidades de la aplicación web

  Background:
    Given requerimientos

  Scenario: Iniciar partida
    When ingreso la palabra "elefante" en el campo de búsqueda
    And hago clic en el botón de enviar
    Then debería ver la palabra con la misma cantidad de guiones bajos que letras