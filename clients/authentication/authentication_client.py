from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class Token(TypedDict):
    """
    Описание структуры аутентификационных токенов.
    """
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseDict(TypedDict):
    """
    Описание структуры ответа аутентификации.
    """
    token: Token


class RefreshRequestDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str  # Название ключа совпадает с API


class Authentification(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    pass

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentification/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()


def get_authentification_client() -> Authentification:
    """
    Функция создает экземпляр Authentification у уже встроенным HTTP-клиентом.

    :return: Готовый к использованию Authentification
    """
    return Authentification(client=get_public_http_client())
