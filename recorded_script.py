import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://v2.zenclass.in/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("YOUR_EMAIL")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").press("CapsLock")
    page.get_by_role("textbox", name="Password").fill("YOUR_PASSWORD")
    page.get_by_role("textbox", name="Password").press("CapsLock")
    page.get_by_role("textbox", name="Password").fill("YOUR_PASSWORD")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Close popup").click()
    page.get_by_text("Resaba A").nth(1).click()
    page.get_by_text("Log out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)