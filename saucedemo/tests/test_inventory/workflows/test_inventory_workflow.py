from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_inventory_page_loads_correctly(page):
    inventory = InventoryPage(page)
    inventory.open()
    inventory.verify_inventory_loaded()

def test_item_names_are_not_empty(page):
    inventory = InventoryPage(page)
    item_names = inventory.get_item_names()
    assert all(name.strip() != "" for name in item_names), "Some item names are empty"