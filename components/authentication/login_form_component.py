from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # атрибуты/ локаторы стр
        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

        # реализация самого метода заполнения формы
        # название метода формируется так:
        # 1. действие(нажать, проверить)
        # 2. контекст(с чем работаем логин/регистрация/ какая форма)
        # 3. элемент тайп - с чем конкретно - кнопка / поле и т.д.

    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)  # проверка, что поле реально заполнено

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text('Wrong email or password')
