from pathlib import Path

from selenium.webdriver.common.by import By

from automation.core.file_utils import *
from automation.core.helper import get_resources_dir_path
from automation.core.wait import until
from automation.page_objects.base_page import BasePage

DOWNLOAD_PATH = '{}/Downloads'.format(str(Path.home()))


class InvoiceDownloadPage(BasePage):
    DOWNLOAD_PDF = (By.XPATH, '//a[contains(text(), "PDF")]')

    def __init__(self, driver):
        super().__init__(driver)
        self.downloaded_file_path = None
        self.pdf_file_name = None

    def download_pdf(self, file_name):
        self.pdf_file_name = '{}.pdf'.format(file_name)
        self.downloaded_file_path = '{}/{}'.format(DOWNLOAD_PATH,
                                                   self.pdf_file_name)

        self.switch_to_window()
        remove_file_if_exists(self.downloaded_file_path)

        self.click(self.get_visible_element(self.DOWNLOAD_PDF))
        self.wait_till_pdf_download(self.downloaded_file_path)

        return self

    @staticmethod
    def wait_till_pdf_download(path):
        until(method=is_file_downloaded, args=path)

    def move_to_resources(self):
        src = self.downloaded_file_path
        dst = '{}/{}'.format(get_resources_dir_path(), self.pdf_file_name)
        move_file_to_path(src, dst)
