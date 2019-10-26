from automation.tests.conftest import validate_element


def test_book_by_region(driver, eyes):
    element = driver.find_element_by_id('pid3')
    validate_element(driver, eyes, element)

