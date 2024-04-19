from requests import get, post, delete, put


class TestApiLanguages:
    def __init__(self, api_key):
        self.api_key = api_key

    def test_get_languages(self):
        # неправильный апи ключ
        print(get(f'http://localhost:8080/api/bad_api_key/languages').json())
        # некорректное значение айди
        print(get(f'http://localhost:8080/api/{self.api_key}/languages/1000').json())
        # некорректный формат айди
        print(get(f'http://localhost:8080/api/{self.api_key}/languages/test').json())

        # правильный апи ключ
        print(get(f'http://localhost:8080/api/{self.api_key}/languages').json())
        # корректный айди
        print(get(f'http://localhost:8080/api/{self.api_key}/languages/1').json())

    def test_post_languages(self):
        # неправильный апи ключ
        print(post('http://localhost:8080/api/bad_key/languages', json={'language': 'C++'}).json())
        # пустой json
        print(post(f'http://localhost:8080/api/{self.api_key}/languages', json={}).json())
        # некорректный json
        print(post(f'http://localhost:8080/api/{self.api_key}/languages', json={'level': 'senior'}).json())
        # неполный json
        print(post(f'http://localhost:8080/api/{self.api_key}/languages',
                   json={'language_title': 'С++'}).json())

        # корректный json
        print(post(f'http://localhost:8080/api/{self.api_key}/languages',
                   json={'language_title': 'С++', 'language_sign': 'C'}).json())
        # проверка добавления
        print(get(f'http://localhost:8080/api/{self.api_key}/languages').json())

    def test_put_languages(self):
        # неправильный апи ключ
        print(put('http://localhost:8080/api/bad_key/languages/1', json={'language': 'C++'}).json())
        # пустой json
        print(put(f'http://localhost:8080/api/{self.api_key}/languages/1', json={}).json())
        # некорректный json
        print(post(f'http://localhost:8080/api/{self.api_key}/languages/1', json={'level': 'senior'}).json())
        # некорректное значение айди
        print(put(f'http://localhost:8080/api/{self.api_key}/languages/1000', json={'language_sign': 'Java'}).json())
        # некорректный формат айди
        print(put(f'http://localhost:8080/api/{self.api_key}/languages/test', json={'language_sign': 'Java'}).json())

        # корректный json
        print(put(f'http://localhost:8080/api/{self.api_key}/languages/1', json={'language_sign': 'Java'}).json())
        # проверка изменения
        print(get(f'http://localhost:8080/api/{self.api_key}/languages').json())

    def test_delete_languages(self):
        # неправильный апи ключ
        print(delete('http://localhost:8080/api/bad_api_key/languages/1').json())
        # некорректное значение айди
        print(delete(f'http://localhost:8080/api/{self.api_key}/languages/1000').json())
        # некорректный формат айди
        print(delete(f'http://localhost:8080/api/{self.api_key}/languages/test').json())

        # корректный айди
        print(delete(f'http://localhost:8080/api/{self.api_key}/languages/1').json())
        # проверка удаления
        print(get(f'http://localhost:8080/api/{self.api_key}/languages').json())

    def all_test_cases(self):
        self.test_get_languages()
        self.test_post_languages()
        self.test_put_languages()
        self.test_delete_languages()


# TestApiLanguages('0e64a536199a9d71e9b7ecddde355ad2').all_test_cases()
# print(post(f'http://localhost:8080/api/584a82ac3dfd1572c1cb9362e5ba8f14/languages',
#                    json={'language_title': 'Python', 'language_sign': 'Python'}).json())
# print(post(f'http://localhost:8080/api/584a82ac3dfd1572c1cb9362e5ba8f14/languages',
#                    json={'language_title': 'Java', 'language_sign': 'Java'}).json())
print(post(f'http://localhost:8080/api/584a82ac3dfd1572c1cb9362e5ba8f14/languages',
                   json={'language_title': 'Kotlin', 'language_sign': 'Kotlin'}).json())