from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv
load_dotenv()

import time


@given('requerimientos')
def requerimientos(context):
    context.driver = webdriver.Chrome()
    context.host = os.getenv('FE_PROJECT_URL')
    context.driver.get(context.host)

@given('ingreso la palabra "{word}"')
def ingresar_palabra(context, word):
    input = context.driver.find_element(By.NAME, "palabra-input")
    input.send_keys(word)
    context.palabra = word
    submit_button = context.driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

@then('debería ver la palabra con la misma cantidad de guiones bajos que letras')
def obtener_cantidad_guiones(context):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.NAME, "palabra-con-guiones")))
    underscores = context.driver.find_element(By.NAME, "palabra-con-guiones")
    value_of_underscores = underscores.get_attribute("value").replace(" ", "")
    assert len(value_of_underscores) == len(context.palabra), "Error, la cantidad de guiones bajos no coinciden"


@when('intento la letra "{letter}"')
def intentar_adivinar_letra(context, letter):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.NAME, "letra-input")))
    input_letter = context.driver.find_element(By.NAME, "letra-input")
    input_letter.send_keys(letter)
    context.letter = letter
    submit_button = context.driver.find_element(By.NAME, "adivinar-letra")
    submit_button.click()

@then('debería ver la letra revelada en la palabra')
def verificar_letra_revelada(context):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.NAME, "palabra-con-guiones")))
    underscores = context.driver.find_element(By.NAME, "palabra-con-guiones")
    word = underscores.get_attribute("value").replace(" ", "")
    assert context.letter in word, f"Error, la letra correcta no está en la palabra"

@then('la cantidad de vidas debería ser "{lives}"')
def verificar_letra_revelada(context, lives):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.NAME, "vidas")))
    remaining_lives = context.driver.find_element(By.NAME, "vidas").get_attribute("value")
    assert lives == remaining_lives, f"Error, la cantidad de vidas es errónea"


@then('debería ver la letra en la letras incorrectas')
def verificar_letra_revelada(context):
    WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.NAME, "letras-incorrectas")))
    incorrect_letters = context.driver.find_element(By.NAME, "letras-incorrectas")
    letters = incorrect_letters.get_attribute("value").replace(" ", "")
    assert context.letter in letters, f"Error, la letra incorrecta no está en las letras incorrectas"

