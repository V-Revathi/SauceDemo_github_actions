from saucedemo.pages.inventory_page import constants
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_inventory_elements_are_visible(page):
    inventory = InventoryPage(page)
    inventory.open()
    inventory.should_display_six_items()
