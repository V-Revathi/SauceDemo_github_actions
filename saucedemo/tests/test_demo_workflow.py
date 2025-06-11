from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
from saucedemo.pages.checkout_overview_page.constants import CHECKOUT_OVERVIEW_URL
from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.login_page import constants
from saucedemo.pages.checkout_overview_page.checkout_overview_page import CheckoutOverviewPage
from playwright.sync_api import expect

def test_workflow(page):
    """
    Test the complete workflow from login to order completion in the SauceDemo application. 
    This test includes logging in, adding an item to the cart, proceeding to checkout,
    filling out the checkout form, and verifying the order completion.
    """
    # Step 1: Login to the application
    login_page = LoginPage(page)
    login_page.login(constants.VALID_USERNAME, constants.VALID_PASSWORD)
    login_page.assert_login_successful()

    # Step 2: Add item to cart
    inventory = InventoryPage(page)
    inventory.open()
    inventory.verify_inventory_loaded()
    inventory.add_first_item_to_cart()
    item_names = inventory.get_item_names()
    assert all(name.strip() != "" for name in item_names), "Some item names are empty"

    # Step 3: Go to cart and proceed to checkout
    cart = CartPage(page)
    cart.open_cart()
    cart.verify_cart_loaded()

    names = cart.get_cart_item_names()
    assert len(names) > 0

    cart.proceed_to_checkout_and_verify()

    # Step 4: Fill checkout form and continue
    checkout = CheckoutPage(page)
    checkout.verify_checkout_page_loaded()
    checkout.verify_form_elements_visible()
    checkout.fill_checkout_info("Revathi", "Venkatachalam", "12345")
    checkout.continue_to_overview()

    # Step 5: Assert navigation to overview page
    expect(page).to_have_url(CHECKOUT_OVERVIEW_URL)

    overview = CheckoutOverviewPage(page)
    overview.verify_overview_loaded()
    overview.finish_checkout()
    overview.verify_order_complete()