from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def current_ur2l(self):
        url2 = self.browser.current_url
        print ("base_page:",url2)
        return url2