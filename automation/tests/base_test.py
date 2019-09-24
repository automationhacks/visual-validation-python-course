from unittest import TestCase

from selenium import webdriver


class BaseTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://applitools.com/helloworld')

    def tearDown(self):
        self.driver.quit()
