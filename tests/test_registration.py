from  playwright.sync_api import expect, Page
import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.registration
@pytest.mark.regression
# чтоб обернуть файл playwright в тест нам надо
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):

    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()

    # dashboard_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    # dashboard_page.check_dashboard_title()

    # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        #
        # email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        # email_input.fill('username@gmail@mail.ru')
        #
        # username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        # username_input.fill('username')
        #
        # password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        # password_input.fill('Password')
        #
        # ##//button[@data-testid="login-page-login-button"]
        # registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        # registration_button.click()
        #
        # dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        # expect(dashboard_title).to_be_visible()