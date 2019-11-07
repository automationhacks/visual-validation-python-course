from selenium.webdriver.common.by import By

from automation.page_objects.base_page import BasePage
from automation.page_objects.invoice_simple.invoice_download_page import \
    InvoiceDownloadPage


class InvoicePage(BasePage):
    FROM_NAME = (By.ID, 'invoice-company-name')
    TO_NAME = (By.ID, 'invoice-client-name')
    ITEM_DESCRIPTION = (By.ID, 'invoice-item-code')
    ITEM_RATE = (By.CSS_SELECTOR, 'td[data-label="Price"] input')
    GET_LINK = (By.CSS_SELECTOR, '.invoice-detail-about button')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_from_and_to_details(self, from_name, to_name):
        sender_name = self.get_visible_element(self.FROM_NAME)
        self.enter_text(sender_name, from_name)

        receiver_name = self.get_visible_element(self.TO_NAME)
        self.enter_text(receiver_name, to_name)
        return self

    def enter_item_with_rate(self, item, rate):
        item_description = self.get_visible_element(self.ITEM_DESCRIPTION)
        self.enter_text(item_description, item)

        item_rate = self.get_visible_element(self.ITEM_RATE)
        self.enter_text(item_rate, rate)
        return self

    def click_on_get_link(self):
        get_link_btn = self.get_visible_element(self.GET_LINK)
        self.click(get_link_btn)
        return InvoiceDownloadPage(self.driver)
