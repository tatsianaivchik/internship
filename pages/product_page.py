from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button[name="add"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product__title h1.h2')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.price-item.price-item--sale bdi')
    VIEW_CART_BTN = (By.CSS_SELECTOR, 'a.button[href="/cart"]')

    def store_product_name_n_price(self):
        self.driver.product_name = self.find_element(*self.PRODUCT_NAME).text
        self.driver.product_price = self.find_element(*self.PRODUCT_PRICE).text

    def add_product_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def click_vew_cart_btn(self):
        self.wait_for_element_appear(self.VIEW_CART_BTN).click()