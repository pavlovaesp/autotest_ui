import pytest

# маркировка x fail, если кейс упал, но мы планируем мониторить его
@pytest.mark.xfail(reason="Баг 4567")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг 455567")
def test_without_bug():
    ...


# xfail ожидаемый фэйл, знаем, что есть баг, мониторит состояние бага
# xpass означает, что баг починили и можно убрать маркировку xfail