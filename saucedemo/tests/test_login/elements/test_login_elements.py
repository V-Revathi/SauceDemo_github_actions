from saucedemo.pages.login_page import locators, constants
from playwright.sync_api import expect

def test_login_page_elements(page):
    page.goto(constants.LOGIN_URL)

    expect(page.locator(locators.LOGIN_USERNAME)).to_be_visible()
    expect(page.locator(locators.LOGIN_PASSWORD)).to_be_visible()
    expect(page.locator(locators.LOGIN_BUTTON)).to_be_visible()
