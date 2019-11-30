from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_basket_page_url(self):
        assert "/basket/" in self.browser.current_url, "URL shoud contains login."

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_basket_has_text_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET)