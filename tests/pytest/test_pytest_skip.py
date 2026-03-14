import pytest

@pytest.mark.skip(reason="Фича в разработке")
def test_feature_in_development():
    ...

@pytest.mark.skip(reason="Проблема с инфраструктурой")
def test_another_feature_1():
    ...


def test_another_feature_2():
    ...