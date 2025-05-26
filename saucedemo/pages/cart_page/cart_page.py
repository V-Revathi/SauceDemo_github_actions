from saucedemo.pages.cart_page import constants, locators
from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page

    def open_cart(self):
        self.page.click(locators.CART_LINK)
        expect(self.page).to_have_url(constants.CART_URL)

    def verify_cart_loaded(self):
        expect(self.page.locator(locators.CART_ITEM)).to_be_visible()

    def get_cart_item_names(self):
        return [el.inner_text() for el in self.page.query_selector_all(locators.CART_ITEM_NAME)]

    def get_cart_item_prices(self):
        return [el.inner_text() for el in self.page.query_selector_all(locators.CART_ITEM_PRICE)]

    def proceed_to_checkout(self):
        self.page.click(locators.CHECKOUT_BUTTON)
