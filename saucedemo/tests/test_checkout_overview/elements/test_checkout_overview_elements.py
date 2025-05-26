from saucedemo.pages.checkout_overview_page import constants, locators
from playwright.sync_api import expect

def test_checkout_overview_elements(page):
    page.goto(constants.CHECKOUT_OVERVIEW_URL)

    expect(page.locator(locators.SUBHEADER)).to_have_text("Checkout: Overview")
    # expect(page.locator(locators.ITEM_SUMMARY)).to_be_visible()
    # expect(page.locator(locators.FINISH_BUTTON)).to_be_visible()
    # expect(page.locator(locators.CANCEL_BUTTON)).to_be_visible()
