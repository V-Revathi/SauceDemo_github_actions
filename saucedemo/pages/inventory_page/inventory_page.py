from saucedemo.pages.inventory_page import constants, locators
from playwright.sync_api import expect

class InventoryPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(constants.INVENTORY_URL)

    def verify_inventory_loaded(self):
        expect(self.page).to_have_url(constants.INVENTORY_URL)
        expect(self.page.locator(locators.INVENTORY_ITEMS)).to_have_count(6)

    def get_item_names(self):
        return [el.inner_text() for el in self.page.query_selector_all(locators.ITEM_NAME)]

    def add_first_item_to_cart(self):
        # Ensure the inventory list is visible
        expect(self.page.locator(".inventory_list")).to_be_visible()

        # Locate the first visible "Add to cart" button by text
        add_button = self.page.locator("button:has-text('Add to cart')").first

        # Confirm it's visible
        expect(add_button).to_be_visible(timeout=5000)

        # Click the button to add the item to the cart
        add_button.click()
