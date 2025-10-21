import pytest
from playwright.sync_api import Page

from pages.courses_list_page import CoursesListPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

@pytest.fixture(scope="function")
def registration_page(initialize_browser_state: Page) -> RegistrationPage:
    return RegistrationPage(page=initialize_browser_state)

@pytest.fixture(scope="function")
def dashboard_page(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)

@pytest.fixture
def courses_list_page(chromium_page: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page)