from sauce_demo_tests.locators import *

class InventoryPage:
    def __init__(self, page):
        self.page = page

    def verify_inventory_elements(self):
       # Check that the page title is correct
        assert self.page.title() == "Swag Labs"

        # Verify the inventory list (product grid) is visible
        assert self.page.locator(INVENTORY_LIST).is_visible()

        # Verify that there are at least 6 inventory items
        assert self.page.locator(INVENTORY_ITEM).count() >= 6

        # Verify that the first product name is visible
        assert self.page.locator(INVENTORY_ITEM_NAME).first.is_visible()

        # Verify that the first product price is visible
        assert self.page.locator(INVENTORY_ITEM_PRICE).first.is_visible()

        # Verify the shopping cart icon is visible
        assert self.page.locator(SHOPPING_CART_ICON).is_visible()

        # Verify the sort/filter dropdown is visible
        assert self.page.locator(PRODUCT_SORT_CONTAINER).is_visible()

        # Verify that the "Add to Cart" button for the first item is visible
        assert self.page.locator(ADD_TO_CART_BUTTON).first.is_visible()

        # Verify the footer copy text is visible
        assert self.page.locator(FOOTER_COPY).is_visible()

        # Verify the application logo is visible
        assert self.page.locator(APP_LOGO).is_visible()
