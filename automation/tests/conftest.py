import pytest
from selenium import webdriver

from automation.core.eyes_manager import EyesManager


@pytest.fixture(scope='module')
def manager(driver):
    eyes_manager = EyesManager(driver)
    yield eyes_manager


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
