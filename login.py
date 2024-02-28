from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import unittest
from unittest import TestCase


class Test2(TestCase):
    LOGIN_EMAIL_INPUT = (By.ID, 'login-email')
    LOGIN_PASSWORD_INPUT = (By.ID, 'login-password')
    # aici definim constantele care sa stocheze valoarea de cautare a selectorului pe care il cautam.Pentru a indica
    # ca o variabila trebuie tratata ca si constanta se folosesc majuscule in denumirea lor

    def setUp(self) -> None:  # -> None inseamna ca aceasta functie nu returneaza nimic explicit. Functiile de
        # configurare teste cum ar fi setUp si tearDown sunt adesea definite sa nu returneze nimic
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://mooc.academiacentral.org/login')

    def tearDown(self) -> None:
        self.chrome.quit()  # aceasta comanda este pentru a inchide browserul

    def test_sign_in_1_(self):
        input_email_login = self.chrome.find_element(*self.LOGIN_EMAIL_INPUT)
        input_email_login.send_keys('tudor.nanu10@gmail.com')
        self.assertTrue(input_email_login.is_displayed(), 'Mesajul afisat este corect')
    def test_sign_in_2_(self):
        #aici am testat introducerea emailului setat
        input_password_login = self.chrome.find_element(*self.LOGIN_PASSWORD_INPUT)
        input_password_login.send_keys('Universitate10')
        #aici am testat introducerea parolei setate