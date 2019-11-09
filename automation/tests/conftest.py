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


@pytest.fixture(scope='function')
def setup_test(request, manager):
    test_info = request.param

    _set_batch_and_app_in_manager(manager, test_info)
    _launch_app_and_open_eyes(manager, request, test_info)

    yield manager
    manager.close_eyes()


def _launch_app_and_open_eyes(manager, request, test_info):
    driver = manager.driver
    driver.get(test_info.app_under_test)
    driver.maximize_window()

    test_name = request.function.__name__
    manager.open_eyes(test_name)


def _set_batch_and_app_in_manager(manager, test_info):
    batch_name = test_info.batch_name

    if batch_name:
        manager.set_batch(batch_name)
    manager.set_app_name(test_info.app_name)
