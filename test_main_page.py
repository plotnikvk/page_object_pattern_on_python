import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


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
