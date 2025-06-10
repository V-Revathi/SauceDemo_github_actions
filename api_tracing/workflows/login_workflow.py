from pages.login_page import LoginPage
# from elements.selectors import InventoryPageSelectors

def login(page):
    login_page = LoginPage(page)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    # page.wait_for_selector(InventoryPageSelectors.INVENTORY_LIST)
