from applitools.common import BatchInfo
from applitools.selenium import Eyes

from automation.config.base import APPLITOOLS_API_KEY


class EyesManager:
    def __init__(self, driver):
        self.app_name = None
        self.driver = driver
        self.eyes = self.initialize_eyes()

    @staticmethod
    def initialize_eyes():
        eyes = Eyes()
        eyes.api_key = APPLITOOLS_API_KEY
        return eyes

    def set_app_name(self, app_name):
        self.app_name = app_name

    def set_batch(self, batch_name):
        if batch_name:
            batch_info = BatchInfo(batch_name)
            self.eyes.batch = batch_info

    def validate_window(self, tag=None, full_page=False):
        if full_page:
            self.eyes.force_full_page_screenshot = True

        self.eyes.check_window(tag=tag)

    def validate_element(self, element, tag=None):
        self.eyes.check_region(element, tag=tag)

    def validate_frame(self, frame_reference, region, tag=None):
        self.eyes.check_region_in_frame(frame_reference, region, tag=tag)

    def open_eyes(self, test_name):
        self.eyes.open(self.driver, self.app_name,
                       test_name=test_name)

    def close_eyes(self):
        self.eyes.close()
