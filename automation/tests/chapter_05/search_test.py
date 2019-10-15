from assertpy import assert_that

from automation.tests.conftest import open_eyes, validate_window, close_eyes
from automation.page_objects.search_page import SearchPage


def test_filter_book(eyes, driver):
    page = SearchPage(driver)

    page.filter_books('Agile')
    result = page.verify_visible_books_by_title('Agile Testing')
    assert_that(result).is_equal_to(True)

    validate_window(driver, eyes, tag='filter_text')



