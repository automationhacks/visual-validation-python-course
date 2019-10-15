from automation.tests.conftest import *


def test_hello_world(driver, eyes):
    validate_window(driver, eyes, tag='hello_world')
    driver.find_element_by_css_selector('button').click()
    validate_window(driver, eyes, 'click_me')
