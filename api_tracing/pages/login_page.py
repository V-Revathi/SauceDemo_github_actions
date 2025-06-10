from elements.selectors import LoginPageSelectors

class LoginPage:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        self.page.fill(LoginPageSelectors.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.page.fill(LoginPageSelectors.PASSWORD_INPUT, password)

    def click_login(self):
        self.page.click(LoginPageSelectors.LOGIN_BUTTON)
