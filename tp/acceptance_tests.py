import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from dotenv import load_dotenv

load_dotenv()

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.host = os.getenv('FE_PROJECT_URL')

    def test_first_page_play(self):
        driver = self.driver
        driver.get(self.host)
        try:
            elem = driver.find_element(By.NAME, "palabra-input")
            self.assertIsNotNone(elem, "El elemento no es nulo, por lo tanto, existe en la página.")
        except NoSuchElementException:
            # Manejar la excepción si el elemento no se encuentra
            self.fail("El elemento NO existe en la página.")

    def test_choosen_word_length(self):
        driver = self.driver
        driver.get(self.host)

        word = "carrera"
        input = driver.find_element(By.NAME, "palabra-input")
        input.send_keys(word)
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "palabraConGuionesBajo")))

        underscores = driver.find_element(By.ID, "palabraConGuionesBajo")
        value_of_underscores = underscores.get_attribute("value").replace(" ", "")
        self.assertEqual(len(value_of_underscores), len(word))


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()