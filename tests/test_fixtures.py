from symtable import Class

import pytest

# как объявляются фикстуры, по сути это те же функции, но над которыми стоит декоратор
# фикстуры нужны для автоматизации отправки каких-то данных/ автоматизации создания ТД/ чтоб не
# дублировать код/ готовить данные перед тестом, а потом удалять его по завершению кейса
# автоматизировать открытие браузера для всех классов, а не прописывать в кодеБ кейс выполняет
# только логику, подготовка выносится в фикстуры

@pytest.fixture(autouse=True) # автоматически запускается на каждый кейс и не передается в логах
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные на сервис аналитики")

# scope имеет несколько значений > session, package(запускает один раз на пакет),
# class(один раз на класс), function(один раз на функцию/используется по дефолту)
@pytest.fixture(scope="session") #session запускает один раз на всю сессию
def settings():
    print("[SESSION] Инициализирует настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создает данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")# можно не прописывать, идет по дефолту
def browser():
    print("[FUNCTION] Открываем браузер на каждый автотест")

# фикстура передается в аргументы функции
class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...
