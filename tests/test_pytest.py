 # название функции должно начинаться с test, чтоб pytest валидировал ее
def test_user_login():
     print("Hello!")

# тестовые классы нужны для группировки
# в pytest не должно быть в классах конструкторов
class TestUserLogin:
    def test_1(self):
        ...

    def test_2(self):
        ...

# assert внутри функции может быть несколько, т.е несколько проверок на один бизнес сценарий
def test_assert_positive_case():
    assert (2 + 2) == 4

def test_assert_negative_case():
    assert (2 + 2) == 5, "(2 + 2) != 5"