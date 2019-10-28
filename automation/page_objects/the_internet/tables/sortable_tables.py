from time import sleep
from selenium.webdriver.common.by import By


class SortableTablePage:
    BASE_HEADER = '//table[@id="table1"]/descendant::span[text()="{}"]/parent::th'
    FIRST_NAME = (
        By.XPATH, BASE_HEADER.format('First Name'))
    LAST_NAME = (
        By.XPATH, BASE_HEADER.format("Last Name"))

    def __init__(self, driver):
        self.driver = driver

    def sort_by_first_name(self):
        locator = self.FIRST_NAME
        self.driver.find_element(*locator).click()
        sleep(5)

    def sort_by_last_name(self):
        locator = self.LAST_NAME
        self.driver.find_element(*locator).click()
        sleep(5)
