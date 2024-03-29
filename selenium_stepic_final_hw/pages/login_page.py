from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not found on page url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not found on page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not found on page"

    def register_new_user(self, email, password):
        self.browser.find_element_by_id("id_registration-email").send_keys(email)
        self.browser.find_element_by_id("id_registration-password1").send_keys(password)
        self.browser.find_element_by_id("id_registration-password2").send_keys(password)
        self.browser.find_element_by_css_selector('button[name="registration_submit"]').click()
