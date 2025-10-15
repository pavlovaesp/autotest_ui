# файл, где мы инициализируем фикстуры и отсюда их бере pytest
# название файла только такое

import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

# @pytest.fixture
# def chromium_page() -> Page:   # возвращает тип Page
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)  ## False когда хотим видеть открытый браузер
#         yield browser.new_page()
#         browser.close()

# yield позволяет выполнить действия до и после теста
# При первом вызове выполнение начинается с начала функции до первого yield. После этого функция «замораживает» своё состояние.
# При следующем вызове выполнение продолжается сразу после yield. Каждое значение, которое возвращает yield, становится элементом итерации.
# Когда инструкции заканчиваются, генератор выбрасывает исключение StopIteration — программа понимает, что элементы закончились, и останавливает работу.

import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture
def chromium_page(playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('username@gmail@mail.ru')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('Password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    #page.wait_for_timeout(3000)

    context.storage_state(path='browser-state.json')
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page     # ✅ теперь возвращаем страницу
    context.close()
    browser.close()
