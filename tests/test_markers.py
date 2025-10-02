import pytest

#Декоратор в Python — это функция, которая принимает другую функцию в качестве аргумента, начинается с @
@pytest.mark.smoke # тест промаркерован для смоука и его можно запустить по этой маркеровке в терминале
def test_some_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...


#маркировку можно поставить на класс и на функцию внутри класса
@pytest.mark.smoke
class TestSuite:
    @pytest.mark.smoke
    def test_case1(self):
        ...

    def test_case2(self):
        ...

# эта маркировка действует на все внутри класса
# маркировок может быть несколько
@pytest.mark.ui
class TestUserInterface:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login(self):
        pass

    @pytest.mark.regression
    def test_password_reset(self):
        pass

    @pytest.mark.smoke
    def test_logout(self):
        pass



@pytest.mark.regression
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass