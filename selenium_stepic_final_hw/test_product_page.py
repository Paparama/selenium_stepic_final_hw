import time

import pytest

from final_hw.selenium_stepic_final_hw.pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.links import *


def open_page_and_add_product(browser, link):
    page = open_product_page(browser, link)
    page.add_to_basket()
    return page


def open_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    return page


class TestUserAddToCartFromProductPage(object):

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        reg_page = LoginPage(browser=browser, url=login_link)
        reg_page.open()
        reg_page.register_new_user(str(time.time()) + "ololo@kokoko.ru", "123#@!qweEWQ")
        reg_page.should_be_authorized_user()

    @pytest.mark.parametrize('link', [product_code_at_work_with_promo_link])
    def test_user_can_add_product_to_cart(self, browser, link):
        page = open_page_and_add_product(browser, link)
        page.solve_quiz_and_get_code()
        page.should_be_add_message()
        page.should_be_price()

    @pytest.mark.parametrize('link', [product_code_at_work_link])
    def test_user_cant_see_success_message(self, browser, link):
        page = open_product_page(browser, link)
        page.should_not_be_success_message()

    @pytest.mark.skip(reason="don't should work")
    @pytest.mark.parametrize('link', [product_code_at_work_link])
    def test_message_disappeared_after_adding_product_to_cart(self, browser, link):
        page = open_page_and_add_product(browser, link)
        page.should_be_disappeared_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [product_code_at_work_with_promo_link])
def test_guest_can_add_product_to_cart(browser, link):
    page = open_page_and_add_product(browser, link)
    page.solve_quiz_and_get_code()
    page.should_be_add_message()
    page.should_be_price()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [product_city_and_the_stars_link])
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = CartPage(browser=page.browser, url=page.url)
    basket_page.should_be_cart_is_empty_message()
    basket_page.should_be_cart_is_emptyt()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [product_city_and_the_stars_link])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = open_product_page(browser, link)
    page.go_to_login_page()
    login_page = LoginPage(browser=page.browser, url=page.browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', [product_city_and_the_stars_link])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = open_product_page(browser, link)
    page.go_to_login_page()
    login_page = LoginPage(browser=page.browser, url=page.browser.current_url)
    login_page.should_be_login_link()
