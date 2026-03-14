import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные на сервис аналитики")


@pytest.fixture(scope="session")
def settings():
    print("Инициализируем настройки автотестов")


@pytest.fixture(scope="function")
def users_client():
    print("[FUNCTION] Создает API клиент на каждый вызов теста")


@pytest.fixture(scope="class")
def user():
    print("[Class] Создает данные пользователя один раз на тестовый класс")


class TestUserFlow:
    def test_user_can_login(self, users_client, user, settings):
        ...

    def test_user_can_create_course(self, users_client, user, settings):
        ...


class TestAccountFlow:
    def test_user_account(self, users_client, user, settings):
        ...


@pytest.fixture
def user_data():
    print("Создаем пользователя до теста (setup)")  # Подготавливаем данные для теста
    yield {"username": "test_user", "email": "test@gmail.com"}  # выполняется сам тест (Отдали данные в тест и ожидаем)
    print("Удаляем после теста (teardown)")  # очищаем данные после теста


def test_user_email(user_data):
    assert user_data["email"] == "test@gmail.com"


def test_user_username(user_data):
    assert user_data["username"] == "test_user"
