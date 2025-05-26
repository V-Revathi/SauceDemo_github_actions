from saucedemo.pages.checkout_overview_page import constants, locators
from playwright.sync_api import expect

class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page

    def verify_overview_loaded(self):
        expect(self.page).to_have_url(constants.CHECKOUT_OVERVIEW_URL)
        expect(self.page.locator(locators.SUBHEADER)).to_have_text("Checkout: Overview")
        expect(self.page.locator(locators.ITEM_SUMMARY)).to_be_visible()

    def finish_checkout(self):
        self.page.click(locators.FINISH_BUTTON)

    def cancel_checkout(self):
        self.page.click(locators.CANCEL_BUTTON)
