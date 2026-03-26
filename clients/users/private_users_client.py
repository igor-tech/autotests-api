from httpx import Response

from clients.api_client import APIClient
from clients.api_coverage import tracker
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
import allure

from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    @allure.step("Get user me")
    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}/me")
    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx_lesson.Response
        """
        return self.get(f"{APIRoutes.USERS}/me")

    @allure.step("Get user me by id: {user_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}/{{user_id}}")
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx_lesson.Response
        """
        return self.get(f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Update user by id: {user_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}/{{user_id}}")
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param request: словарь с опциональными полями email, lastName, firstName, middleName
        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx_lesson.Response
        """
        return self.patch(f"{APIRoutes.USERS}/{user_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete user by id: {user_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.USERS}/{{user_id}}")
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx_lesson.Response
        """
        return self.delete(f"{APIRoutes.USERS}/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создает экземпляр PrivateUsersClient у уже встроенным HTTP-клиентом.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
