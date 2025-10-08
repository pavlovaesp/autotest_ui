import pytest

@pytest.mark.skip(reason="Фича в разработке") # skip для пропуска какого-то кейса, например он понадобится еще, но не нужен сейчас
# в скобках пишем причину скипа
# просто так вешать скип плохо, должна быть оправданная причина
# упал сервис, фича в разработке, проблема с инфрой, не ясно будет ли нужна функциональность еще не принято решение
def test_feature_in_development():
    ...


@pytest.mark.skip(reason="Фича в разработке")
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        ...

    def test_feature_in_development_2(self):
        ...