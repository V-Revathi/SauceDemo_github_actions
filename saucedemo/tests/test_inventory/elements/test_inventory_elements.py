from saucedemo.pages.inventory_page import locators, constants
from playwright.sync_api import expect

def test_inventory_elements_are_visible(page):
    page.goto(constants.INVENTORY_URL)

    # Expect 6 items to be visible
    items = page.locator(locators.INVENTORY_ITEMS)
    expect(items).to_have_count(6)

    # Check if item names and "Add to cart" buttons are visible for each item
    for i in range(6):
        item_name = page.locator(f".inventory_item:nth-child({i + 1}) {locators.ITEM_NAME}")
        add_to_cart_button = page.locator(f".inventory_item:nth-child({i + 1}) button")

        expect(item_name).to_be_visible()
        expect(add_to_cart_button).to_be_visible()
