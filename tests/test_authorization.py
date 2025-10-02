from  playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.authentication
def test_wrong_email_or_password__authorization():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)  ## False когда хотим видеть открытый браузер
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        ##//div[@data-testid="login-form-email-input"]//div/input - локатор со страницы
        # правильно использовать упрощенные локаторы
        # используем функцию get_by_test_id и эту часть локатора значение > "login-form-email-input"
        # в случае с почтой/паролем мы указываем imput так как надо искать внутри контейнера
        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.name@gmail@mail.ru')

        ##//div[@data-testid="login-form-password-input"]//div/input
        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill('Password')

        ##//button[@data-testid="login-page-login-button"]
        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        ##//div[@data-testid="login-page-wrong-email-or-password-alert"]
        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()  ##visible виден/ hiden невидем
        expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

        page.wait_for_timeout(3000)  # в реальных проектах таймаут не используется, только если для демо
        # тратит время, тормозит кейс

