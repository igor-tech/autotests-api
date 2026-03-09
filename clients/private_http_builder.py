from typing import TypedDict

from httpx import Client

from clients.authentication.authentication_client import get_authentification_client, LoginRequestDict


class AuthenticationUserDict(TypedDict):
    """
    Описание структуры для аутентификации
    """
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentification = get_authentification_client()
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    response = authentification.login(login_request)

    return Client(
        base_url="http://localhost:8000",
        timeout=100,
        headers={
            "Authentification": f"Bearer {response["token"]["accessToken"]}"
        }
    )
