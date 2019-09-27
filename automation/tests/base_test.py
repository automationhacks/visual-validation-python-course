from unittest import TestCase

from applitools.common import MatchLevel
from applitools.selenium import Eyes
from selenium import webdriver

from automation.config.base import APPLITOOLS_API_KEY


class BaseTest(TestCase):
    def setup(self, test_name):
        self.driver = webdriver.Chrome()
        self.driver.get('https://applitools.com/helloworld')
        self.eyes = self.open_eyes(test_name)

    def teardown(self):
        self.driver.quit()
        self.close_eyes()

    def open_eyes(self, test_name):
        self.eyes = Eyes()
        self.eyes.api_key = APPLITOOLS_API_KEY

        self.eyes.match_level = MatchLevel.STRICT
        self.eyes.open(self.driver, app_name='hello_world',
                       test_name=test_name)

        return self.eyes

    def close_eyes(self):
        self.eyes.close()

    def validate_window(self, tag):
        self.eyes.check_window(tag)
