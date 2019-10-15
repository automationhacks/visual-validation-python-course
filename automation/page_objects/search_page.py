class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def filter_books(self, search_text):
        element = self.driver.find_element_by_id('searchBar')
        element.send_keys(search_text)

    def verify_visible_books_by_title(self, expected_title):
        elements = self.driver.find_elements_by_css_selector(
            '#productList li a h2')
        for element in elements:
            if expected_title in element.text:
                return True

        return False
