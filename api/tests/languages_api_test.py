from requests import get, post, delete, put, patch


# Тест API для ЯП
class TestApiLanguages:
    def __init__(self, host: str, port: str, api_key: str):
        self.host = host
        self.port = port
        self.api_key = api_key

    def test_get_languages(self):
        # неправильный апи ключ
        print(get(f"http://{self.host}:{self.port}/api/bad_api_key/languages").json())
        # некорректное значение айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1000").json())
        # некорректный формат айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/test").json())

        # правильный апи ключ
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/languages").json())
        # корректный айди
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1").json())

    def test_post_languages(self):
        # неправильный апи ключ
        print(post(f"http://{self.host}:{self.port}/api/bad_key/languages",
                   json={"language": "C++"}).json())
        # пустой json
        print(post(f"http://{self.host}:{self.port}/api/{self.api_key}/languages", json={}).json())
        # некорректный json
        print(post(f"http://{self.host}:{self.port}/api/{self.api_key}/languages", json={"level": "senior"}).json())
        # неполный json
        print(post(f"http://{self.host}:{self.port}/api/{self.api_key}/languages",
                   json={"language_title": "С++"}).json())

        # корректный json
        print(post(f"http://{self.host}:{self.port}/api/{self.api_key}/languages",
                   json={"language_title": "С++", "language_sign": "C"}).json())
        # проверка добавления
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/languages").json())

    def test_patch_languages(self):
        # неправильный апи ключ
        print(patch(f"http://{self.host}:{self.port}/api/bad_key/languages/1", json={"language": "C++"}).json())
        # пустой json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1", json={}).json())
        # некорректный json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1",
                    json={"level": "senior"}).json())
        # некорректное значение айди
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1000",
                    json={"language_sign": "Java"}).json())
        # некорректный формат айди
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/test",
                    json={"language_sign": "Java"}).json())

        # корректный json
        print(patch(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1",
                    json={"language_sign": "Java"}).json())
        # проверка изменения
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/languages").json())

    def test_put_languages(self):
        # неправильный апи ключ
        print(put(f"http://{self.host}:{self.port}/api/bad_key/languages/1", json={"language": "C++"}).json())
        # пустой json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1", json={}).json())
        # некорректный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1",
                  json={"level": "senior"}).json())
        # некорректное значение айди
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1000",
                  json={"language_sign": "Java"}).json())
        # некорректный формат айди
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/test",
                  json={"language_sign": "Java"}).json())

        # корректный, но не полный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1",
                  json={"language_sign": "Java"}).json())
        # корректный и полный json
        print(put(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/2",
                  json={"language_sign": "C", "language_title": "C/C++"}).json())
        # проверка изменения
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/languages").json())

    def test_delete_languages(self):
        # неправильный апи ключ
        print(delete(f"http://{self.host}:{self.port}/api/bad_api_key/languages/1").json())
        # некорректное значение айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1000").json())
        # некорректный формат айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/test").json())

        # корректный айди
        print(delete(f"http://{self.host}:{self.port}/api/{self.api_key}/languages/1").json())
        # проверка удаления
        print(get(f"http://{self.host}:{self.port}/api/{self.api_key}/languages").json())

    def all_test_cases(self):
        self.test_get_languages()
        self.test_post_languages()
        self.test_patch_languages()
        self.test_put_languages()
        self.test_delete_languages()
