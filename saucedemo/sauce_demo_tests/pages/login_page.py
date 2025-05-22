from sauce_demo_tests.locators import *

class LoginPage:
    def __init__(self, page):
        self.page = page    # Initialize the page object 

    def login(self, username, password):
        """
        Log in to the SauceDemo website using the provided username and password.

        This method performs the following steps:
        1. Navigates to the SauceDemo login page.
        2. Fills in the username and password fields with the provided credentials.
        3. Clicks the login button.
        4. Asserts that the login was successful by checking the URL.
        """
        self.page.goto("https://www.saucedemo.com/v1/index.html")
        self.page.fill(LOGIN_USERNAME, username)
        self.page.fill(LOGIN_PASSWORD, password)
        self.page.click(LOGIN_BUTTON)
        assert "/inventory.html" in self.page.url
