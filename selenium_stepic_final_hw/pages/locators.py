from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE_ENG = (By.CSS_SELECTOR, "p.price_color")
    ADDING_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    TOTAL_PRICE_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]')
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.basket-mini')


class CartPageLocators(object):
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    CART_WITH_ITEMS = (By.CSS_SELECTOR, "div.basket-title >div > h2")
