from saucedemo.pages.checkout_page import constants, locators
from playwright.sync_api import expect

def test_checkout_form_elements_visible(page):
    page.goto(constants.CHECKOUT_STEP_ONE_URL)

    expect(page.locator(locators.FIRST_NAME_INPUT)).to_be_visible()
    expect(page.locator(locators.LAST_NAME_INPUT)).to_be_visible()
    expect(page.locator(locators.POSTAL_CODE_INPUT)).to_be_visible()
    expect(page.locator(locators.CONTINUE_BUTTON)).to_be_visible()
    expect(page.locator(locators.CANCEL_BUTTON)).to_be_visible()
