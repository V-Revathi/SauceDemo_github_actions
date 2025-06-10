from saucedemo.pages.checkout_page.checkout_page import CheckoutPage
from saucedemo.pages.checkout_page import constants

def test_checkout_form_elements_visible(page):
    page.goto(constants.CHECKOUT_STEP_ONE_URL)
    checkout_page = CheckoutPage(page)

    checkout_page.verify_checkout_page_loaded()
    checkout_page.verify_form_elements_visible()
