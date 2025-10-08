import pytest

@pytest.fixture
def clear_books_database() -> None:
    print("[FIXTURE] Удаляем все данные из базы данных")

@pytest.fixture
def fill_books_database() -> None:
    print("[FIXTURE] Создаем новые данные")

@pytest.mark.usefixtures("fill_books_database")
def test_read_all_books_in_library():
    print("Reading all books in library")

# чтоб не прописывать в каждой функции фикстуру, выводим ее в декораторе
# важно в каком порядке фикстуры, т.к. у них есть своя логика
@pytest.mark.usefixtures(
    "clear_books_database",
    "fill_books_database"
)
class TestLibrary:
    def test_read_books_in_library(self):
        ...

    def test_delete_books_in_library(self):
        ...