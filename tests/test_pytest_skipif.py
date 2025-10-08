import pytest

#маркировка skipif позволяет пропускать кейсы с условием
#условие пишем в скобках, например, версия на которой запускается кейс,
# версия библиотеки, версия системы, версия браузер и т.д.

SYSTEM_VERSION = "v.1.2.0"

@pytest.mark.skipif(
    SYSTEM_VERSION == "v.1.3.0", #SYSTEM_VERSION = "v.1.3.0" = false
    reason="Тест не может быть запущен на версии системы v1.3.0"
)
def test_system_version_valid():
    ...


@pytest.mark.skipif(
    SYSTEM_VERSION == "v.1.2.0",#SYSTEM_VERSION = "v.1.3.0" = true
    reason = "Тест не может быть запущен на версии системы v1.2.0"
)
def test_system_version_invalid():
    ...