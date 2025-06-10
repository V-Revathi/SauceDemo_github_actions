from saucedemo.pages.inventory_page.inventory_page import InventoryPage
from saucedemo.pages.cart_page.cart_page import CartPage
from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
from saucedemo.pages.checkout_overview_page.checkout_overview_page import CheckoutOverviewPage
from playwright.sync_api import expect

def test_complete_checkout_workflow(page):
    overview = CheckoutOverviewPage(page)
    overview.verify_overview_loaded()
    overview.finish_checkout()
    overview.verify_order_complete()

