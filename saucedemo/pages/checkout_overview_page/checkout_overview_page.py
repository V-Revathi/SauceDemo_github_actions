from saucedemo.pages.checkout_overview_page import constants
from saucedemo.pages.checkout_overview_page.locators import CheckoutOverviewPageLocators as locators
from playwright.sync_api import expect

class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page

    def verify_overview_loaded(self):
        expect(self.page).to_have_url(constants.CHECKOUT_OVERVIEW_URL)
        expect(self.page.locator(locators.SUBHEADER)).to_have_text("Checkout: Overview")

    def verify_buttons_visible(self):
        expect(self.page.locator(locators.FINISH_BUTTON)).to_be_visible()
        expect(self.page.locator(locators.CANCEL_BUTTON)).to_be_visible()

    def finish_checkout(self):
        self.page.click(locators.FINISH_BUTTON)

    def cancel_checkout(self):
        self.page.click(locators.CANCEL_BUTTON)

    def verify_order_complete(self):
        expect(self.page).to_have_url(constants.FINISH_URL)
        expect(self.page.locator(locators.COMPLETE_HEADER)).to_have_text("THANK YOU FOR YOUR ORDER")
