from .locators import ProductPageLocators, MainPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def press_submit_button(self):
        self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON).click()

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*MainPageLocators.WATCH_BASKET_BUTTON)
        basket_link.click()

    def check_price(self, price):
        fact_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price == fact_price, "Price is different!"

    def check_name_of_product(self, name_of_product):
        fact_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        assert name_of_product == fact_name, "The name is different!"

    def check_add_of_product(self, expect_message):
        fact_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text
        assert expect_message == fact_message, "The message is different!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is appeared, but should not be"