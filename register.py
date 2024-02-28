from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
#import unittest
from unittest import TestCase

class Test(TestCase):
    FULL_NAME_INPUT = (By.ID, 'register-name')
    PUBLIC_USERNAME_INPUT = (By.ID, 'register-username')
    EMAIL_INPUT = (By.ID, 'register-email')
    PASSWORD_INPUT = (By.ID, 'register-password')
    COUNTRY_OR_REGION_OF_RESIDENCE_INPUT = (By.ID, 'register-country')
    CREATE_ACCOUNT_BTN = (By.XPATH, '//*[@id="register"]/button')


     # aici definim constantele care sa stocheze valoarea de cautare a selectorului pe care il cautam.Pentru a indica
    # ca o variabila trebuie tratata ca si constanta se folosesc majuscule in denumirea lor

    def setUp(self) -> None: # -> None inseamna ca aceasta functie nu returneaza nimic explicit. Functiile de
        #configurare teste cum ar fi setUp si tearDown sunt adesea definite sa nu returneze nimic
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://mooc.academiacentral.org/register')

    def tearDown(self) -> None:
        self.chrome.quit() #aceasta comanda este pentru a inchide browserul

    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://mooc.academiacentral.org/register'
        self.assertEqual(actual, expected, 'The page is not correct')
        #aici am verificat daca poate fi accesat website-ul

    def test_register_1_(self):
        input_full_name = self.chrome.find_element(*self.FULL_NAME_INPUT)
        input_full_name.send_keys('Tudor Nanu')
        self.assertTrue(input_full_name.is_displayed(), 'Mesajul afisat este corect')
        #aici am testat introducerea numelui complet al studentului
    def test_register_2_(self):
        input_public_username= self.chrome.find_element(*self.PUBLIC_USERNAME_INPUT)
        input_public_username.send_keys('2743891090')
        self.assertTrue(input_public_username.is_displayed(), 'Mesajul afisat este corect')
        #aici am testat introducerea codului de student
    def test_register_3_(self):
        input_email = self.chrome.find_element(*self.EMAIL_INPUT)
        input_email.send_keys('tudor.nanu10@gmail.com')
        self.assertTrue(input_email.is_displayed(), 'Mesajul afisat este corect')
        #aici am testat introducerea emailului studentului
    def test_register_4_(self):
        input_password = self.chrome.find_element(*self.PASSWORD_INPUT)
        input_password.send_keys('Universitate10')
        self.assertTrue(input_password.is_displayed(), 'Mesajul afisat este corect')
        #aici am testat introducerea parolei
    def test_register_5_(self):
        input_country = self.chrome.find_element(*self.COUNTRY_OR_REGION_OF_RESIDENCE_INPUT)
        input_country.send_keys('Romania')
        self.assertTrue(input_country.is_displayed(),'Mesajul afisat este corect')
        #aici am testat introducerea tarii studentului







