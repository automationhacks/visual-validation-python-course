from selenium.webdriver.common.by import By

from automation.tests.conftest import validate_element, validate_frame


def test_book_by_region(driver, eyes):
    element = driver.find_element_by_id('pid3')
    validate_element(driver, eyes, element)


def test_element_in_frame(driver, eyes):
    frame = driver.find_element(By.TAG_NAME, 'iframe')
    validate_frame(driver, eyes, frame, (By.ID, 'tinymce'))
