from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_add_item_and_checkout(page):
    inventory = InventoryPage(page)
    inventory.open()
    inventory.add_first_item_to_cart()

    cart = CartPage(page)
    cart.open_cart()
    cart.verify_cart_loaded()

    names = cart.get_cart_item_names()
    assert len(names) > 0

    with page.expect_navigation():
        cart.proceed_to_checkout()

    expect(page).to_have_url("https://www.saucedemo.com/v1/checkout-step-one.html", timeout=5000)
