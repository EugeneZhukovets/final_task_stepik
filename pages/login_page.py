from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.current_ur2l()
        assert url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", f"URL NOW ={url}"
        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LoginPageForm), "Login-form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.RegisterFrom), "Register-form is not presented"



        