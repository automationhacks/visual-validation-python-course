import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_visible_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator))

    @staticmethod
    def enter_text(element, text):
        element.send_keys(text)

    @staticmethod
    def click(element):
        element.click()

    def switch_to_window(self, index=1):
        handles = self.driver.window_handles

        if len(handles) == 1:
            WebDriverWait(self.driver, 30).until(self.open_windows_gt_one)

        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    @staticmethod
    def open_windows_gt_one(driver):
        return len(driver.window_handles) > 1
