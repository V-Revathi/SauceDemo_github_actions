from saucedemo.pages.login_page import constants
from saucedemo.pages.login_page.locators import LoginPageLocators
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(constants.LOGIN_URL)
     
    def should_have_login_username(self):
        expect(self.page.locator(LoginPageLocators.LOGIN_USERNAME)).to_be_visible()

    def should_have_login_password(self):
        expect(self.page.locator(LoginPageLocators.LOGIN_PASSWORD)).to_be_visible()

    def should_have_login_button(self):
        expect(self.page.locator(LoginPageLocators.LOGIN_BUTTON)).to_be_visible()

    def fill_username(self, username):
        self.page.fill(LoginPageLocators.LOGIN_USERNAME, username)

    def fill_password(self, password):
        self.page.fill(LoginPageLocators.LOGIN_PASSWORD, password)

    def submit(self):
        self.page.click(LoginPageLocators.LOGIN_BUTTON)

    def login(self, username, password):
        self.open()
        self.fill_username(username)
        self.fill_password(password)
        self.submit()
        
    def assert_login_successful(self):
        expect(self.page).to_have_url(constants.INVENTORY_URL)

