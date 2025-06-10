from saucedemo.pages.login_page.login_page import LoginPage

def test_login_page_elements(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.should_have_login_username()
    login_page.should_have_login_password()
    login_page.should_have_login_button()
