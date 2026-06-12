from playwright.sync_api import Page 
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
    def open_login_page(self):
        self.page.goto("https://v2.zenclass.in/login")
    def login(self, email, password):
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click() 