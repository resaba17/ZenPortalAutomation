from pages.login_page import LoginPage 
from pages.dashboard_page import DashboardPage 

def test_logout(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    login.open_login_page()
    login.login("YOUR_EMAIL",YOUR_PASSWORD")
    page.wait_for_timeout(5000)

    #dashboard.close_popup()
    dashboard.logout()
    page.wait_for_timeout(3000)


    assert "login" in page.url.lower()
