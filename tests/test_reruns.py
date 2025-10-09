import random
import pytest

PLATFORM = "Windows"

# reruns сколько раз перезапустить, reruns_delay промежуток между перезапусками
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    assert  random.choice([True, False])

# если не хотим перезапускать все тесты класса, то ставим маркировку к
# конкретному кейсу
@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_reruns_1(self):
        assert random.choice([True, False])


    def test_reruns_2(self):
        assert random.choice([True, False])

# условие для перезапуска
@pytest.mark.flaky(reruns=3, reruns_delay=2, conditions=PLATFORM == "Windows")
def test_rerun_with_condition():
    assert random.choice([True, False])