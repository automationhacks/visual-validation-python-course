from automation.tests.conftest import *


def test_hello_world(driver, eyes):
    open_eyes(driver, eyes)
    validate_window(eyes, tag='hello_world')
    driver.find_element_by_css_selector('button').click()
    validate_window(eyes, 'click_me')
