from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FORM), "Login email form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FORM), "Login password form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FORM), "Register email form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FORM), \
            "Register password form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FORM), \
            "Register password confirm form is not presented"