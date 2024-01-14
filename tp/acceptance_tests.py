import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
        # self.assertIn("Python", driver.title)
        try:
            elem = driver.find_element(By.NAME, "palabra-input")
            self.assertIsNotNone(elem, "El elemento no es nulo, por lo tanto, existe en la página.")
        except NoSuchElementException:
            # Manejar la excepción si el elemento no se encuentra
            self.fail("El elemento NO existe en la página.")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()