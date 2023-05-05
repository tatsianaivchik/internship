from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):

    NUM_ITEMS_IN_CART = (By.CSS_SELECTOR, 'div.cart-count-bubble span')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'a.cart-item__name.link')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.price.price--end bdi')

    def num_items_in_cart(self, expected_num):
        self.verify_text(expected_num, *self.NUM_ITEMS_IN_CART)

    def verify_product_name_n_price(self):
        self.verify_text(self.driver.product_name, *self.PRODUCT_NAME)
        product_price_in_cart = self.find_elements(*self.PRODUCT_PRICE)
        assert product_price_in_cart[1].text == self.driver.product_price
        # self.verify_text(self.driver.product_price, *self.PRODUCT_PRICE)

