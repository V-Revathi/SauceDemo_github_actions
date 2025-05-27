# # from saucedemo.pages.inventory_page.inventory_page import InventoryPage
# # from saucedemo.pages.cart_page.cart_page import CartPage
# # from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
# # from playwright.sync_api import expect

# # def test_checkout_form_submission(page):
# #     # Add an item
# #     inventory = InventoryPage(page)
# #     inventory.open()
# #     inventory.add_first_item_to_cart()

# #     # Go to cart
# #     cart = CartPage(page)
# #     cart.open_cart()
# #     cart.proceed_to_checkout()

# #     # Fill checkout info
# #     checkout = CheckoutPage(page)
# #     checkout.verify_checkout_page_loaded()
# #     checkout.fill_checkout_info("Revathi", "Venkatachalam", "12345")
# #     checkout.continue_to_overview()

# #     expect(page).to_have_url("**/checkout-step-two.html")

# # tests/test_checkout_page/test_checkout_form_submission.py

# from saucedemo.pages.login_page.login_page import LoginPage
# from saucedemo.pages.inventory_page.inventory_page import InventoryPage
# from saucedemo.pages.cart_page.cart_page import CartPage
# from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
# from saucedemo.pages.login_page import constants as login_constants
# from saucedemo.pages.checkout_overview_page.constants import CHECKOUT_OVERVIEW_URL
# from playwright.sync_api import expect

# def test_checkout_form_submission(page):
#     # Step 1: Log in
#     login = LoginPage(page)
#     login.open()
#     login.login(login_constants.VALID_USERNAME, login_constants.VALID_PASSWORD)

#     # Step 2: Add item to cart
#     inventory = InventoryPage(page)
#     inventory.add_first_item_to_cart()

#     # Step 3: Go to cart and proceed to checkout
#     cart = CartPage(page)
#     cart.open_cart()
#     cart.proceed_to_checkout_and_verify()

#     # Step 4: Fill checkout form and continue
#     checkout = CheckoutPage(page)
#     checkout.verify_checkout_page_loaded()
#     checkout.verify_form_elements_visible()
#     checkout.fill_checkout_info("Revathi", "Venkatachalam", "12345")
#     checkout.continue_to_overview()

#     # # Step 5: Assert navigation to overview page
#     expect(page).to_have_url(CHECKOUT_OVERVIEW_URL)

from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
from saucedemo.pages.checkout_overview_page.constants import CHECKOUT_OVERVIEW_URL
from playwright.sync_api import expect

def test_checkout_form_submission(page):
    # Step 1: Add item to cart
    inventory = InventoryPage(page)
    inventory.open()
    inventory.add_first_item_to_cart()

    # Step 2: Go to cart and proceed to checkout
    cart = CartPage(page)
    cart.open_cart()
    cart.proceed_to_checkout_and_verify()

    # Step 3: Fill checkout form and continue
    checkout = CheckoutPage(page)
    checkout.verify_checkout_page_loaded()
    checkout.verify_form_elements_visible()
    checkout.fill_checkout_info("Revathi", "Venkatachalam", "12345")
    checkout.continue_to_overview()

    # Step 4: Assert navigation to overview page
    expect(page).to_have_url(CHECKOUT_OVERVIEW_URL)
