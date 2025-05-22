import pytest
from playwright.sync_api import sync_playwright
from sauce_demo_tests.pages.login_page import LoginPage
from sauce_demo_tests.pages.inventory_page import InventoryPage

@pytest.fixture(scope="class")
def setup_browser():
    """
    Fixture to launch the browser, open a new page, and yield it for use in test methods.
    The browser will be closed after the test completes.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def login(setup_browser):
    """
    Fixture to log in to the SauceDemo site using the LoginPage class.
    This fixture interacts with the login page, enters credentials, and performs the login.
    """
    page = setup_browser
    login_page = LoginPage(page)  
    login_page.login("standard_user", "secret_sauce")
    return page

class TestSauceDemo:
    """
    Test class containing test cases for login functionality and inventory page validation.
    """
    def test_login(self, login):
        """
        Test to validate successful login by checking the page title.
        """
        page = login
        assert page.title() == "Swag Labs"

    def test_inventory_page_elements(self, login):
        """
        Test to validate various UI elements on the inventory page.
        Uses the InventoryPage POM class to check all expected components.
        """
        page = login
        inventory_page = InventoryPage(page)  
        inventory_page.verify_inventory_elements()
