from  playwright.sync_api import expect, Page
import pytest
from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.authentication
@pytest.mark.parametrize(
    'email, password',
    [
        ('user.name@gmail.com', 'password'),
        ('user.name@gmail.com','  '),
        ('  ', 'password')
    ]
)

# в скобках метода идет инициализация фикстур
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    #login_page = LoginPage(page=chromium_page) - строка не нужна т.к. мы сделали фикстуру pages с методом login_page и добавили ее в плагины
    # ниже используем PageObject(это паттерн, который говорит как мы должны работать со страницыми) -
    # base_page(база PageObject), login_page> Задача PageObject убрать дубли в коде, сделать его более логичным и читабельным
    # visit вызываем base_page
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # ниже вызываем login_page
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()


        # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        #
        # ##//div[@data-testid="login-form-email-input"]//div/input - локатор со страницы
        # # правильно использовать упрощенные локаторы
        # # используем функцию get_by_test_id и эту часть локатора значение > "login-form-email-input"
        # # в случае с почтой/паролем мы указываем imput так как надо искать внутри контейнера
        # email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        # email_input.fill(email)
        #
        # ##//div[@data-testid="login-form-password-input"]//div/input
        # password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        # password_input.fill(password)
        #
        # ##//button[@data-testid="login-page-login-button"]
        # login_button = chromium_page.get_by_test_id('login-page-login-button')
        # login_button.click()
        #
        # ##//div[@data-testid="login-page-wrong-email-or-password-alert"]
        # wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        # expect(wrong_email_or_password_alert).to_be_visible()  ##visible виден/ hiden невидем
        # expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
        #
        # chromium_page.wait_for_timeout(3000)  # в реальных проектах таймаут не используется, только если для демо
        # # тратит время, тормозит кейс

