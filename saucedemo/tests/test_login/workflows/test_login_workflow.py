from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.login_page import constants
from playwright.sync_api import expect

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.login(constants.VALID_USERNAME, constants.VALID_PASSWORD)

    # expect(page).to_have_url("**/inventory.html")
    expect(page).to_have_url("https://www.saucedemo.com/v1/inventory.html")
    # expect(page.locator(".product_label")).to_have_text("Products")

