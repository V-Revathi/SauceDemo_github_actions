from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.cart_page.cart_page import CartPage
from playwright.sync_api import expect
from saucedemo.pages.login_page import constants 

def test_cart_elements_visibility(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(constants.VALID_USERNAME, constants.VALID_PASSWORD)

    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()

    cart = CartPage(page)
    cart.open_cart()
    cart.verify_cart_loaded()
    cart.verify_cart_contents()
