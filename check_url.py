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
        self.chrome.get('https://www.academiacentral.org/online-certificates/inclusive-and-ethical-leadership-certificate/')

    def tearDown(self) -> None:
        self.chrome.quit()  # aceasta comanda este pentru a inchide browserul

    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://www.academiacentral.org/online-certificates/inclusive-and-ethical-leadership-certificate/'
        self.assertEqual(actual, expected, 'The page is not correct')
        #aici am verificat daca poate fi accesat website-ul

    def setUp(self) -> None:  # -> None inseamna ca aceasta functie nu returneaza nimic explicit. Functiile de
        # configurare teste cum ar fi setUp si tearDown sunt adesea definite sa nu returneze nimic
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.academiacentral.org/contact/')



    def tearDown(self) -> None:
        self.chrome.quit()  # aceasta comanda este pentru a inchide browserul

    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://www.academiacentral.org/contact/'
        #aici am verificat daca poate fi accesat website-ul



    def test_website_click(self):
        actual = self.chrome.current_url
        expected = 'https://www.academiacentral.org/contact/'
        self.assertEqual(actual, expected, 'The page is not correct')
        if actual:
            print("This section is for contact the institution")
        else:
            print("Error 404, page not found")

    def test_website_blog(self):
        actual = 'https://www.academiacentral.org/blog/'
        if actual:
            print("This section is for access the blog")
        else:
            print("Error 404, page not found")

    def test_website_faq(self):
        actual= 'https://www.academiacentral.org/frequently-asked-questions/'
        if actual:
            print("This section is for access the FAQs")
        else:
            print("Error 404, page not found")

