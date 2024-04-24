from requests import get, post, delete, put, patch


# Тест API для проектов
class TestApiProjects:
    def __init__(self, host: str, port: str, api_key: str):
        self.host = host
        self.port = port
        self.api_key = api_key

    def test_get_projects(self):
        # неправильный апи ключ
        print(get(f"http://{self.host}:{self.port}/api/bad_api_key/projects").json())
        # некорректное значение айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1000").json())
        # некорректный формат айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/test").json())

        # правильный апи ключ
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/projects").json())
        # корректный айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1").json())

    def test_post_projects(self):
        # не предполагается API
        pass

    def test_patch_projects(self):
        # неправильный апи ключ
        print(patch(f"http://{self.host}:{self.port}/api/bad_key/projects/1",
                    json={"about": "PROJECT ABOUT NEW"}).json())
        # пустой json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1", json={}).json())
        # некорректный json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1", json={"level": "senior"}).json())
        # некорректное значение айди
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1000",
                    json={"about": "PROJECT ABOUT NEW"}).json())
        # некорректный формат айди
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/test",
                    json={"about": "PROJECT ABOUT NEW"}).json())

        # корректный json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1",
                    json={"about": "PROJECT ABOUT NEW"}).json())
        # проверка изменения
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/projects").json())

    def test_put_projects(self):
        # неправильный апи ключ
        print(put(f"http://{self.host}:{self.port}/api/bad_key/projects/1",
                  json={
                      "about": "PROJECT ABOUT NEW",
                      "title": "PROJECT TITLE NEW",
                      "is_visible": True,
                      "language_id": 1,
                      "price": 1000,
                      "user_id": 1
                  }).json())
        # пустой json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1", json={}).json())
        # некорректный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1",
                  json={"email": "USER_1@MAIL.com"}).json())
        # некорректное значение айди
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1000",
                  json={
                      "about": "PROJECT ABOUT NEW",
                      "title": "PROJECT TITLE NEW",
                      "is_visible": True,
                      "language_id": 1,
                      "price": 1000,
                      "user_id": 1
                  }).json())
        # некорректный формат айди
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/test",
                  json={
                      "about": "PROJECT ABOUT NEW",
                      "title": "PROJECT TITLE NEW",
                      "is_visible": True,
                      "language_id": 1,
                      "price": 1000,
                      "user_id": 1
                  }).json())

        # корректный, но не полный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1",
                  json={
                      "about": "PROJECT ABOUT NEW",
                      "title": "PROJECT TITLE NEW"
                  }).json())
        # корректный и полный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/2",
                  json={
                      "about": "PROJECT ABOUT NEW",
                      "title": "PROJECT TITLE NEW",
                      "is_visible": True,
                      "language_id": 1,
                      "price": 1000,
                      "user_id": 1
                  }).json())
        # проверка изменения
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/projects").json())

    def test_delete_projects(self):
        # неправильный апи ключ
        print(delete(f"http://{self.host}:{self.port}/api/bad_api_key/projects/1").json())
        # некорректное значение айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1000").json())
        # некорректный формат айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/test").json())

        # корректный айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/projects/1").json())
        # проверка удаления
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/projects").json())

    def test_all_cases(self):
        self.test_get_projects()
        self.test_post_projects()
        self.test_patch_projects()
        self.test_put_projects()
        self.test_delete_projects()
