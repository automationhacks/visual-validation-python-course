import pytest
import assertpy

from automation.page_objects.invoice_simple.invoice_page import InvoicePage

APP_UNDER_TEST = 'https://app.invoicesimple.com/'
EXPECTED_FILE_NAME = 'INV0001'


@pytest.fixture(autouse=True)
def setup(manager):
    driver = manager.driver
    driver.get(APP_UNDER_TEST)
    driver.maximize_window()

    yield manager


def test_pdf(setup):
    invoice_page = InvoicePage(setup.driver)
    invoice_page \
        .enter_from_and_to_details('Gaurav', 'Rob') \
        .enter_item_with_rate('Comics', '10') \
        .click_on_get_link() \
        .download_pdf(EXPECTED_FILE_NAME) \
        .move_to_resources()

    result = setup.validate_pdf()
    assertpy.assert_that(result).does_not_contain('Mismatch')
