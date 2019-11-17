from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def press_submit_button(self):
        self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON).click()

    def check_price(self, price):
        fact_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price in fact_price, "Price is different!"

    def check_name_of_product(self, name_of_product):
        fact_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        assert name_of_product == fact_name, "The name is different!"