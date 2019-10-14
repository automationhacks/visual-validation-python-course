import pytest
from applitools.selenium import Eyes
from selenium import webdriver

from automation.config.base import APPLITOOLS_API_KEY

APP_NAME = 'hello_world'


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://applitools.com/helloworld')
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def eyes(driver):
    eyes = initialize_eyes()
    yield eyes
    eyes.close()


def initialize_eyes():
    eyes = Eyes()
    eyes.api_key = APPLITOOLS_API_KEY
    return eyes


def open_eyes(driver, eyes):
    eyes.open(driver, APP_NAME, test_name=get_test_name())


def validate_window(eyes, tag):
    eyes.check_window(tag)


def get_test_name():
    import inspect
    return inspect.stack()[2].function
