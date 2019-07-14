from .base_page import BasePage
from .locators import CartPageLocators
from .messages import CartPageMessages


class CartPage(BasePage):
    def should_be_cart_is_empty_message(self):
        assert self.is_element_present(*CartPageLocators.CART_EMPTY_TEXT), \
            "Success message is presented, but should not be"
        assert self.browser.find_element(*CartPageLocators.CART_EMPTY_TEXT).text == CartPageMessages.empty_cart_text()

    def should_be_cart_is_emptyt(self):
        assert self.is_not_element_present(*CartPageLocators.CART_WITH_ITEMS), "There are some items to bye"
