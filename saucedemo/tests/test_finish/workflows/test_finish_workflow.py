from saucedemo.pages.finish_page.finish_page import FinishPage
from saucedemo.pages.finish_page import constants
from playwright.sync_api import expect

def test_finish_page(page):
    page.goto(constants.FINISH_URL)
    finish = FinishPage(page)
    
    expect(page).to_have_url("https://www.saucedemo.com/v1/checkout-complete.html")
