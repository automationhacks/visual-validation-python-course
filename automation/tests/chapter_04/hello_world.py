from automation.tests.base_test import BaseTest


class HelloWorldTest(BaseTest):

    def test_hello_world(self):
        self.setup(test_name=self._testMethodName)

        self.validate_window(tag='hello_world')
        self.driver.find_element_by_css_selector('button').click()
        self.validate_window('click_me')

        self.teardown()
