import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1]) # передаем в списке числа которые нужно проверить, соответсвенно тест
# будет запущен 4 раза в данном случае
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['windows', 'linux', 'debian'])
@pytest.mark.parametrize('browsers', ['os', 'windows', 'linux', 'debian'])
def test_multiplication_of_numbers(os: str, browsers: str):
    assert  len(browsers) > 0

@pytest.fixture(params=['os', 'windows', 'linux', 'debian'])
def browsers(request: SubRequest): # в request=аргумент, системный аргумент внутри
    # которого хранится вся инфа по фикстуре и хранится параметр, которым параметризирована
    # данная текстура. SubRequest это тип реквеста
    return request.param #param это атрибут в котором
    # храняться значения params =['os', 'windows', 'linux', 'debian']

# когда надо параметризировать саму фикстуру
def test_open_browser(browser: str):
    print(f'opening browser: {browser}')

# pytest параметризирует класс и распространяет это параметризацию на
# функции внутри/ часто используют например на dev и test стендах или на разных юзерах
@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperational:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operational(self, user: str, account: str):
        print(f'User with operations: {user}')

    def test_user_without_operational(self, user: str):
        print(f'User without operations: {user}')

# если параметризирован и класс и тест внутри класса проверки перемножаются


# идентификаторы

users = {  # словарь
    '+70000000009': 'User with money on bank account',
    '+70000000010': 'User without money on bank account',
    '+70000000012': 'User with operations money on bank account'
}
# Цель лямбда-функций — обеспечить лаконичный способ определения временных функций,
# которые используются только один раз или как часть более крупной функции
@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'       # динамический идентификатор
)
def test_identifiers(phone_number: str):
    ...
