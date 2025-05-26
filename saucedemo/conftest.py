# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()

# @pytest.fixture(scope="function")
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     context.close()

import pytest
from playwright.sync_api import sync_playwright
from saucedemo.pages.login_page.login_page import LoginPage
from saucedemo.pages.login_page.constants import VALID_USERNAME, VALID_PASSWORD, LOGIN_URL

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    page = context.new_page()
    
    # Perform login once
    page.goto(LOGIN_URL)
    login = LoginPage(page)
    login.login(VALID_USERNAME, VALID_PASSWORD)
    
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()
