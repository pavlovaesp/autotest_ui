# файл, где мы инициализируем фикстуры и отсюда их бере pytest
# название файла только такое

import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture
def chromium_page() -> Page:   # возвращает тип Page
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)  ## False когда хотим видеть открытый браузер
        yield browser.new_page()
        browser.close()

# yield позволяет выполнить действия до и после теста