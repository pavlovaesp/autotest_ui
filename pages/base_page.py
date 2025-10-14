from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page): # конструктор
        self.page = page

# реализация базового метода применимого к любой странице
# метод который заменяет goto, посещение какой-либо страницы
# на вход метод принимает ссылку, далее через self обращаемся к page
    def visit(self, url: str):
        self.page.goto(url, wait_until= 'networkidle')

    def reload(self):
        self.page.reload(wait_until= 'networkidle')