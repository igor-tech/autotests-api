from httpx import Client

from clients.event_hooks import curl_event_hook


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx_lesson.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx_lesson.Client.
    """
    return Client(
        base_url="http://localhost:8000",
        timeout=100,
        event_hooks={"request": [curl_event_hook]}
    )
