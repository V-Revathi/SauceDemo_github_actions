from saucedemo.pages.login_page import constants, locators
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(constants.LOGIN_URL)

    def fill_username(self, username):
        self.page.fill(locators.LOGIN_USERNAME, username)

    def fill_password(self, password):
        self.page.fill(locators.LOGIN_PASSWORD, password)

    def submit(self):
        self.page.click(locators.LOGIN_BUTTON)

    def login(self, username, password):
        self.open()
        self.fill_username(username)
        self.fill_password(password)
        self.submit()
        