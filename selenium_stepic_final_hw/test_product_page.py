import pytest

from final_hw.selenium_stepic_final_hw.pages.login_page import LoginPage
from .pages.product_page import ProductPage


def open_page_and_add_product(browser, link):
    page = open_page(browser, link)
    page.add_to_basket()
    return page


def open_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    return page


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    page = open_page_and_add_product(browser, link)
    page.solve_quiz_and_get_code()
    page.should_be_add_message()
    page.should_be_price()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser, link):
    page = open_page_and_add_product(browser, link)
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_guest_cant_see_success_message(browser, link):
    page = open_page(browser, link)
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"])
def test_message_disappeared_after_adding_product_to_cart(browser, link):
    page = open_page_and_add_product(browser, link)
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = open_page(browser, link)
    page.go_to_login_page()
    login_page = LoginPage(browser=page.browser, url=page.browser.current_url)
    login_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = open_page(browser, link)
    page.go_to_login_page()
    login_page = LoginPage(browser=page.browser, url=page.browser.current_url)
    login_page.should_be_login_page()
