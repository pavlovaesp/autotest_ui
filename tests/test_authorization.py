from  playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.authentication
@pytest.mark.parametrize('email, password', [('user.name@gmail.com', 'password'), ('user.name@gmail.com','  '), ('  ', 'password')])
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        ##//div[@data-testid="login-form-email-input"]//div/input - локатор со страницы
        # правильно использовать упрощенные локаторы
        # используем функцию get_by_test_id и эту часть локатора значение > "login-form-email-input"
        # в случае с почтой/паролем мы указываем imput так как надо искать внутри контейнера
        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill(email)

        ##//div[@data-testid="login-form-password-input"]//div/input
        password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill(password)

        ##//button[@data-testid="login-page-login-button"]
        login_button = chromium_page.get_by_test_id('login-page-login-button')
        login_button.click()

        ##//div[@data-testid="login-page-wrong-email-or-password-alert"]
        wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()  ##visible виден/ hiden невидем
        expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

        chromium_page.wait_for_timeout(3000)  # в реальных проектах таймаут не используется, только если для демо
        # тратит время, тормозит кейс

