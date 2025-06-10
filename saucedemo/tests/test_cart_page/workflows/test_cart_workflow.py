from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage

def test_add_item_and_checkout(page):
    inventory = InventoryPage(page)
    inventory.open()
    inventory.add_first_item_to_cart()

    cart = CartPage(page)
    cart.open_cart()
    cart.verify_cart_loaded()

    names = cart.get_cart_item_names()
    assert len(names) > 0

    cart.proceed_to_checkout_and_verify()
