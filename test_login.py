from pages.login_page import LoginPage
def test_successful_login(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login("YOUR_EMAIL","YOUR_PASSWORD")
    page.wait_for_timeout(5000)
    assert "dashboard"in page.url.lower() 
