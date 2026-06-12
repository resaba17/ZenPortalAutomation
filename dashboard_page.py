from playwright.sync_api import Page
class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
    def logout(self):
        self.page.wait_for_timeout(5000)
        self.page.locator(".avatar-profile-name").click()
        self.page.get_by_text("Log out").click() 