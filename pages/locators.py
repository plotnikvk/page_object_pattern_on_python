from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    WATCH_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR,"div.product_main h1")
    PRODUCT_ADDED = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div.alert:nth-child(1)")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")
