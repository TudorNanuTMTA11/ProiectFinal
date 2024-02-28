import unittest
from unittest import TestCase
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner

from ProiectFinal.register import Test
from ProiectFinal.login import Test2
from ProiectFinal.check_url import Test2

class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test2)
        ])
        # runner = HTMLTestRunner(log=True, verbosity=2,output='report', title='Test report', report_name= 'report',
        #                         open_in_browser=True,description='HTMLTestreport',tested_by='Tudor')
        # runner.run(teste_de_rulat)
        with open("Test_report.txt", 'w') as f:
            runner = unittest.TextTestRunner(f, verbosity=2)
            runner.run(teste_de_rulat)



