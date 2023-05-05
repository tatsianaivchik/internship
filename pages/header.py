from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_ICON = (By.CSS_SELECTOR, 'search-modal.header__search summary.header__icon--search')
    SEARCH_FIELD = (By.ID, 'Search-In-Modal')
    SEARCH_RESULT = (By.CSS_SELECTOR, '#predictive-search-results-list li a[href*="{TEXT}"]')
    SEARCH_FOR_BUTTON = (By.ID, 'predictive-search-option-search-keywords')
    SEARCH_PRODUCT_ITEM = (By.CSS_SELECTOR, '#predictive-search-option-1 span.h4')

    def click_on_search(self):
        # self.click(*self.SEARCH_ICON)
        search_icon = self.find_elements(*self.SEARCH_ICON)
        search_icon[1].click()

    def input_search_text(self, text):
        search_field_input = self.find_elements(*self.SEARCH_FIELD)
        search_field_input[1].send_keys(text)

    def get_search_text_locator(self, text):
        return [self.SEARCH_RESULT[0], self.SEARCH_RESULT[1].replace("{TEXT}", text)]

    def verify_text_search(self, text):
        locator = self.get_search_text_locator(text)
        self.wait_for_element_appear(locator)

        self.verify_partial_text(text, *self.SEARCH_FOR_BUTTON)
        self.click(*self.SEARCH_FOR_BUTTON)

    def click_on_first_product(self):
        self.wait_for_element_appear(self.SEARCH_PRODUCT_ITEM).click()
