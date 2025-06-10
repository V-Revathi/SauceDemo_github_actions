from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.login_page import constants
from playwright.sync_api import expect

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.login(constants.VALID_USERNAME, constants.VALID_PASSWORD)
    login_page.assert_login_successful()
