from typing import TypedDict, NotRequired

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: NotRequired[str]
    lastName: NotRequired[str]
    firstName: NotRequired[str]
    middleName: NotRequired[str]


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/me/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param request: словарь с опциональными полями email, lastName, firstName, middleName
        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/me/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/me/{user_id}")


def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Функция создает экземпляр PrivateUsersClient у уже встроенным HTTP-клиентом.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
