# pages/inventory_page/inventory_page.py

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

        # In inventory_page.py
    def add_first_item_to_cart(self):
        # self.page.locator("button").nth(0).click()
        self.page.locator("button[data-test='add-to-cart-sauce-labs-backpack']").click()


