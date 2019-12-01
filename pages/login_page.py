from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "URL shoud contains login."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.NEW_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.NEW_REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_NEW_REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
