from selenium.webdriver.common.by import By
from selenium import webdriver

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LoginPageLink = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LoginPageForm = (By.ID, "login_form")
    RegisterFrom = (By.ID, "register_form")
