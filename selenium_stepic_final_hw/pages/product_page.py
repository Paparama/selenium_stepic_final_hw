import math

from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators
from .messages import ProductPageMessages


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_be_add_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert self.browser.find_element(*ProductPageLocators.ADDING_MESSAGE).text == ProductPageMessages.eng_add(book_name)

    def should_be_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_ENG).text
        assert self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_MESSAGE).text == ProductPageMessages.eng_total_price(price)
        assert price in self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDING_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDING_MESSAGE), \
            "Success message is presented, but should not be"
