from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False) ## False когда хотим видеть открытый браузер
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'

    )

    # локатор не найден на странице
    #unknown = page.locator('#unknown')
    #expect(unknown).to_be_visible()

    # пытаемся ввести текст в кнопку/ неправильное взаимодействие с элементом
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # элемент еще не появился на странице/ возникает когда не блока сверху wait с ожиданием загрузки вех эл-ов на стр
    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'text'
        """
    )

    page.wait_for_timeout(4000)