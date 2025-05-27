from saucedemo.pages.finish_page import constants, locators
from playwright.sync_api import expect

def test_finish_page_elements(page):
    page.goto(constants.FINISH_URL)

    expect(page.locator(locators.COMPLETE_HEADER)).to_have_text("THANK YOU FOR YOUR ORDER")
