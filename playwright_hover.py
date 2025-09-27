from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False) ## False когда хотим видеть открытый браузер
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    #//div[@data-testid="login-page-registration-link"]//div/input
    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.hover()

    page.wait_for_timeout(4000)