from  playwright.sync_api import expect, Page
import pytest
from pages.registration_page import RegistrationFormComponent, RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.registration
@pytest.mark.regression
# чтоб обернуть файл playwright в тест нам надо
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):

    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.check_visible()
    registration_page.registration_form.fill_registration_form(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    registration_page.registration_form.click_registration_button()
    dashboard_page.dashboard.check_visible_dashboard_title()

