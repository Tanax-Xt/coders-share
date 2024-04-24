from requests import get, post, delete, put, patch


# Тест API для пользователей
class TestApiUsers:
    def __init__(self, host: str, port: str, api_key: str):
        self.host = host
        self.port = port
        self.api_key = api_key

    def test_get_users(self):
        # неправильный апи ключ
        print(get(f"http://{self.host}:{self.port}/api/bad_api_key/users").json())
        # некорректное значение айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1000").json())
        # некорректный формат айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/users/test").json())

        # правильный апи ключ
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/users").json())
        # корректный айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1").json())

    def test_post_users(self):
        # неправильный апи ключ
        print(post(f"http://{self.host}:{self.port}/api/bad_key/users",
                   json={
                       "password": "USERPASSWORD",
                       "email": "USER@MAIL.com",
                       "name": "USERNAME",
                   }).json())
        # пустой json
        print(post(f"http://{self.host}:{self.port}/api/{self.api_key}/users", json={}).json())
        # некорректный json
        print(post(f"http://{self.host}:{self.port}/api/{self.api_key}/users", json={"level": "senior"}).json())
        # неполный json
        print(post(f"http://{self.host}:{self.port}/api/{self.api_key}/users",
                   json={"name": "USERNAME"}).json())

        # корректный json
        print(post(f"http://{self.host}:{self.port}/api/{self.api_key}/users",
                   json={
                       "password": "USERPASSWORD",
                       "email": "USER@MAIL.com",
                       "name": "USERNAME",
                   }).json())
        # проверка добавления
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/users").json())

    def test_patch_users(self):
        # неправильный апи ключ
        print(patch(f"http://{self.host}:{self.port}/api/bad_key/users/1",
                    json={"name": "USERNAME_1"}).json())
        # пустой json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1", json={}).json())
        # некорректный json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1", json={"level": "senior"}).json())
        # некорректное значение айди
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1000",
                    json={"name": "USERNAME_1"}).json())
        # некорректный формат айди
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/users/test",
                    json={"name": "USERNAME_1"}).json())

        # корректный json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1",
                    json={"name": "USERNAME_1"}).json())
        # проверка изменения
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/users").json())

    def test_put_users(self):
        # неправильный апи ключ
        print(put(f"http://{self.host}:{self.port}/api/bad_key/users/1",
                  json={"name": "USERNAME_1", "email": "USER_1@MAIL.com"}).json())
        # пустой json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1", json={}).json())
        # некорректный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1",
                  json={"name": "USERNAME_1", "email": "USER_1@MAIL.com"}).json())
        # некорректное значение айди
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1000",
                  json={"name": "USERNAME_1", "email": "USER_1@MAIL.com"}).json())
        # некорректный формат айди
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/users/test",
                  json={"name": "USERNAME_1", "email": "USER_1@MAIL.com"}).json())

        # корректный, но не полный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1",
                  json={"name": "USERNAME_1"}).json())
        # корректный и полный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/users/2",
                  json={"name": "USERNAME_1", "email": "USER_1@MAIL.com"}).json())
        # проверка изменения
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/users").json())

    def test_delete_users(self):
        # неправильный апи ключ
        print(delete(f"http://{self.host}:{self.port}/api/bad_api_key/users/1").json())
        # некорректное значение айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1000").json())
        # некорректный формат айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/users/test").json())

        # корректный айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/users/1").json())
        # проверка удаления
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/users").json())

    def test_all_cases(self):
        self.test_get_users()
        self.test_post_users()
        self.test_patch_users()
        self.test_put_users()
        self.test_delete_users()
