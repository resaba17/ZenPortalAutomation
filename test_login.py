from pages.login_page import LoginPage
def test_successful_login(page):
    login = LoginPage(page)
    login.open_login_page()
    login.login("resaba723@gmail.com", "Resaba9#")
    page.wait_for_timeout(5000)
    assert "dashboard"in page.url.lower() 