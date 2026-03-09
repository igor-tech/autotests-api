from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx_lesson.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx_lesson.Client.
    """
    return Client(
        base_url="http://localhost:8000",
        timeout=100
    )
