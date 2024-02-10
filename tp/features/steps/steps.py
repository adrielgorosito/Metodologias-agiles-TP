from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import time
# time.sleep(5)  5 segundos

import os
from dotenv import load_dotenv
load_dotenv()

@given('requerimientos')
def given_estoy_en_pagina_inicio(context):
    context.driver = webdriver.Chrome()
    context.host = os.getenv('FE_PROJECT_URL')
    context.driver.get(context.host)

@when('ingreso la palabra "{word}" en el campo de búsqueda')
def ingresar_palabra(context, word):
    input = context.driver.find_element(By.NAME, "palabra-input")
    input.send_keys(word)
    context.palabra = word

@when('hago clic en el botón de enviar')
def click_enviar(context):
    submit_button = context.driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

@then('debería ver la palabra con la misma cantidad de guiones bajos que letras')
def obtener_cantidad_guiones(context):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.ID, "palabraConGuionesBajo")))
    underscores = context.driver.find_element(By.ID, "palabraConGuionesBajo")
    value_of_underscores = underscores.get_attribute("value").replace(" ", "")
    assert len(value_of_underscores) == len(context.palabra), "Error, la cantidad de guiones bajos no coinciden"