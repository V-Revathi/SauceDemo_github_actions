from saucedemo.pages.cart_page import constants
from saucedemo.pages.cart_page.locators import CartPageLocators as locators
from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page

    def open_cart(self):
        self.page.click(locators.CART_LINK)
        expect(self.page).to_have_url(constants.CART_URL)

    def verify_cart_loaded(self):
        assert self.page.locator(locators.CART_ITEM).count() >= 1

    def get_cart_item_names(self):
        return [el.inner_text() for el in self.page.query_selector_all(locators.CART_ITEM_NAME)]

    def get_cart_item_prices(self):
        return [el.inner_text() for el in self.page.query_selector_all(locators.CART_ITEM_PRICE)]

    def proceed_to_checkout_and_verify(self):
       # Wait until the button is visible before clicking
        expect(self.page.locator(locators.CHECKOUT_BUTTON)).to_be_visible()
        
        with self.page.expect_navigation():
            self.page.click(locators.CHECKOUT_BUTTON)

        expect(self.page).to_have_url("https://www.saucedemo.com/v1/checkout-step-one.html", timeout=5000)
    def verify_cart_contents(self):
        """Verify cart contains at least one item and checkout button is visible."""
        
        expect(self.page.locator(locators.CART_ITEM)).to_have_count(1)
        expect(self.page.locator(locators.CART_ITEM_NAME)).to_be_visible()
        expect(self.page.locator(locators.CART_ITEM_PRICE)).to_be_visible()
        expect(self.page.locator(locators.CHECKOUT_BUTTON)).to_be_visible()
