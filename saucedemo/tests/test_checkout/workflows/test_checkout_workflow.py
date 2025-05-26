from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
from playwright.sync_api import expect

def test_checkout_form_submission(page):
    # Add an item
    inventory = InventoryPage(page)
    inventory.open()
    inventory.add_first_item_to_cart()

    # Go to cart
    cart = CartPage(page)
    cart.open_cart()
    cart.proceed_to_checkout()

    # Fill checkout info
    checkout = CheckoutPage(page)
    checkout.verify_checkout_page_loaded()
    checkout.fill_checkout_info("John", "Doe", "12345")
    checkout.continue_to_overview()

    expect(page).to_have_url("**/checkout-step-two.html")
