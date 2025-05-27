from saucedemo.pages.checkout_overview_page.checkout_overview_page import CheckoutOverviewPage
from saucedemo.pages.checkout_overview_page import constants

def test_checkout_overview_elements(page):
    page.goto(constants.CHECKOUT_OVERVIEW_URL)
    overview = CheckoutOverviewPage(page)

    overview.verify_overview_loaded()
    overview.verify_buttons_visible()
