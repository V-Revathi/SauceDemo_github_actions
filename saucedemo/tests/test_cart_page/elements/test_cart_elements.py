from saucedemo.pages.cart_page import constants, locators
from playwright.sync_api import expect

def test_cart_elements_visibility(page):
    page.goto(constants.CART_URL)
    # expect(page.locator(locators.CART_ITEM)).to_have_count(1)  
    expect(page.locator(locators.CHECKOUT_BUTTON)).to_be_visible()
