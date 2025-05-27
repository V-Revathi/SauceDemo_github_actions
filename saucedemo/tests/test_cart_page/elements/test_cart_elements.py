from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.cart_page.cart_page import CartPage
from playwright.sync_api import expect

def test_cart_elements_visibility(page):
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()

    cart = CartPage(page)
    cart.open_cart()

    cart.verify_cart_loaded()
    expect(page.locator(cart.locators.CART_ITEM)).to_have_count(1)
    expect(page.locator(cart.locators.CHECKOUT_BUTTON)).to_be_visible()
