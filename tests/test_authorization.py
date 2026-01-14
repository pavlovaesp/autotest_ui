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
    # не меняем visit() — это метод BasePage
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # ниже вызываем login_page, а login_form это вызов компонентов
    login_page.login_form.fill_login_form(email=email, password=password)
    login_page.login_form.click_login_button()
    login_page.login_form.check_visible_wrong_email_or_password_alert()

