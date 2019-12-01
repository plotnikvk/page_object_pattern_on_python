import pytest
import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket1(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.check_price("£9.99")
    page.check_name_of_product("The shellcoder's handbook")
    page.press_submit_button()
    page.solve_quiz_and_get_code()


def test_guest_can_add_product_to_basket2(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.check_price("£19.99")
    page.check_name_of_product("Coders at Work")
    page.press_submit_button()
    page.solve_quiz_and_get_code()
    page.check_add_of_product("Coders at Work")


@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket3(browser, promo_code):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}'.format(promo_code)
    page = ProductPage(browser, link)
    page.open()
    page.check_price("£19.99")
    page.check_name_of_product("Coders at Work")
    page.press_submit_button()
    page.solve_quiz_and_get_code()
    page.check_add_of_product("Coders at Work")

@pytest.mark.xfail(reason="message sould be")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.check_price("£19.99")
    page.check_name_of_product("Coders at Work")
    page.press_submit_button()
    page.solve_quiz_and_get_code()
    page.check_add_of_product("Coders at Work")
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="message sould be appeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.check_price("£19.99")
    page.check_name_of_product("Coders at Work")
    page.press_submit_button()
    page.solve_quiz_and_get_code()
    page.check_add_of_product("Coders at Work")
    page.should_be_disappeared_success_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page_url()
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_has_text_empty()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user(f"{str(time.time())}@fakemail.com", "pip_pap_pip_1")
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.check_price("£19.99")
        page.check_name_of_product("Coders at Work")
        page.press_submit_button()
        page.solve_quiz_and_get_code()
        page.check_add_of_product("Coders at Work")

    @pytest.mark.need_review
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page_url()
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_basket_has_text_empty()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


