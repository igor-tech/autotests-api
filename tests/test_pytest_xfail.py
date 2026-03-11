import pytest


@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест падает с ошибкой")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="баг уже исправлен, но на тесте все еще висит маркировка xfail")
def test_without_bug():
    ...

@pytest.mark.xfail(reason="внешний сервис не доступен")
def test_external_services_in_unviable():
    assert 1 == 2