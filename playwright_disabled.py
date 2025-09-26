from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright: # открываем контекст
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page() # открываем новую страницу

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()

    page.wait_for_timeout(4000)