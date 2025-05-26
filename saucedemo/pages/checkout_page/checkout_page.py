from saucedemo.pages.checkout_page import constants, locators
from playwright.sync_api import expect

class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def verify_checkout_page_loaded(self):
        expect(self.page).to_have_url(constants.CHECKOUT_STEP_ONE_URL)
        expect(self.page.locator(locators.FIRST_NAME_INPUT)).to_be_visible()
        expect(self.page.locator(locators.LAST_NAME_INPUT)).to_be_visible()
        expect(self.page.locator(locators.POSTAL_CODE_INPUT)).to_be_visible()

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(locators.FIRST_NAME_INPUT, first_name)
        self.page.fill(locators.LAST_NAME_INPUT, last_name)
        self.page.fill(locators.POSTAL_CODE_INPUT, postal_code)

    def continue_to_overview(self):
        self.page.click(locators.CONTINUE_BUTTON)
