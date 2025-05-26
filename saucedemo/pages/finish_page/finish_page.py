from saucedemo.pages.finish_page import constants, locators
from playwright.sync_api import expect

class FinishPage:
    def __init__(self, page):
        self.page = page

    def verify_finish_page_loaded(self):
        expect(self.page).to_have_url(constants.FINISH_URL)
        expect(self.page.locator(locators.COMPLETE_HEADER)).to_have_text("THANK YOU FOR YOUR ORDER")
        expect(self.page.locator(locators.COMPLETE_TEXT)).to_be_visible()
        expect(self.page.locator(locators.BACK_HOME_BUTTON)).to_be_visible()

    def return_to_inventory(self):
        self.page.click(locators.BACK_HOME_BUTTON)
