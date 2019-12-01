from selenium.webdriver.common.by import By

class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    WATCH_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    NEW_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    NEW_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_NEW_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@value='Register']")
    SUCCESS_REGISTRATION = (By.CSS_SELECTOR, ".alert-success")

class ProductPageLocators():
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR,"div.product_main h1")
    PRODUCT_ADDED = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div.alert:nth-child(1)")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")
