# Coders Share 
![last commit](https://img.shields.io/github/last-commit/Tanax-Xt/coders-share) ![license](https://img.shields.io/github/license/Tanax-Xt/coders-share)

Coders Share – это онлайн-площадка для покупки и продажи проектов и их частей

Воспользоваться сервисом можно по ссылке [coders-share-yandexhack.amvera.io](https://coders-share-yandexhack.amvera.io/)


### Содержание
  <ol>
    <li><a href="#ключевые-возможности">Ключевые возможность</a></li>
    <li><a href="#начало-работы">Начало работы</a></li>
    <li><a href="#работа-с-API">Работа с API</a></li>
  </ol>


## Ключевые возможности
* Размещение собственных проектов на продажу
* Приобретение чужих проектов
* Работа с API


## Начало работы

Склонируйте репозиторий:
```sh
git clone https://github.com/Tanax-Xt/coders-share.git
```

Установите необходимые библиотеки:
```sh
pip install -r requirements.txt
```

Создайте `.env` файл в корневой директории и создайте следующие переменные окружения (`HOST` и `PORT` можете поменять на свои):
```dotenv
SECRET_KEY="YOUR_SECRET_KEY"
HOST=localhost
PORT=8080
```

Запустите `app.py`:
```sh
python app.py
```


## Работа с API

### Содержание
  <ol>
    <li><a href="#получение-ключа">Получение ключа</a></li>
    <li><a href="#работа-с-API-ключом">Работа с API-ключом</a></li>
    <li><a href="#работа-с-пользователями">Работа с пользователями</a></li>
    <li><a href="#работа-с-проектами">Работа с проектами</a></li>
    <li><a href="#работа-с-языками-программирования">Работа с языками программирования</a></li>
  </ol>

### Получение ключа
Для получения API-ключа зарегистрируйтесь на сайте и перейдите на страницу `/developer`. Нажмите на кнопку для генерации ключа. Вы получите ключ доступа к API, состоящий из 32 символов 


### Работа с API-ключом
После получения API-ключа вы можете обращаться к API по следующей схеме:

`https://URL/api/your_api_key/data_category`
* `URL` - адрес сайта
* `your_api_key` - ваш API-ключ
* `data_category` - необходима категория данных


### Работа с пользователями
#### Получение всех пользователей:
```text
GET https://URL/api/your_api_key/users
```
Пример ответа:
```json
{
  "users": [
    {
      "added_date": "2024-04-19 20:57:57",
      "email": "ivan@test.com",
      "id": 1,
      "money": 1000,
      "name": "Ivan"
    },
    {
      "added_date": "2024-04-19 21:17:57",
      "email": "danila@test.com",
      "id": 2,
      "money": 0,
      "name": "Danila"
    },
    {
      "added_date": "2024-04-19 22:29:38",
      "email": "user@test.com",
      "id": 3,
      "money": 0,
      "name": "User"
    }
  ]
}
```
#### Получение одного пользователя:
```text
GET https://URL/api/your_api_key/users/1
```
Пример ответа:
```json
{
  "users": {
      "added_date": "2024-04-19 20:57:57",
      "email": "USER@MAIL.com",
      "id": 1,
      "money": 1000,
      "name": "USERNAME"
    }
}
```
#### Добавление пользователя:
```text
POST https://URL/api/your_api_key/users
```
JSON:
```json
{
  "password": "USERPASSWORD",
  "email": "USER@MAIL.com",
  "name": "USERNAME"
}
```
Ответ:
```json
{"success": "OK"}
```
#### Редактирование пользователя `PUT`:
При выполнении запроса `PUT` с неполным json неуказанные поля наменятся на `null`. Доступные поля для изменения запросом: `email`, `name`
```text
PUT https://URL/api/your_api_key/users/1
```
JSON:
```json
{
  "name": "USERNAME_1"
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный пользователь:
```json
{
  "users": {
    "added_date": "2024-04-22 20:36:46",
    "email": null,
    "id": 1,
    "money": 0,
    "name": "USERNAME_1"
  }
}
```
```text
PUT https://URL/api/your_api_key/users/1
```
JSON:
```json
{
  "name": "USERNAME_1",
  "email": "USER_1@MAIL.com"
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный пользователь:
```json
{
  "users": {
    "added_date": "2024-04-22 20:36:46",
    "email": "USER_1@MAIL.com",
    "id": 1,
    "money": 0,
    "name": "USERNAME_1"
  }
}
```
#### Редактирование пользователя `PATCH`:
При выполнении запроса `PATCH` с неполным json поменяются только те поля, которые были указаны. Доступные поля для изменения запросом: `email`, `name`
```text
PATCH https://URL/api/your_api_key/users/1
```
JSON:
```json
{
  "name": "USERNAME_1"
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный пользователь:
```json
{
  "users": {
    "added_date": "2024-04-22 20:36:46",
    "email": "USER@MAIL.com",
    "id": 1,
    "money": 0,
    "name": "USERNAME_1"
  }
}
```


#### Удаления пользователя:
```text
DELETE https://URL/api/your_api_key/users/1
```
Ответ:
```json
{"success": "OK"}
```


### Работа с проектами
#### Получение всех проектов:
```text
GET https://URL/api/your_api_key/projects
```
Пример ответа:
```json
{
  "projects": [
    {
      "about": "test python about",
      "added_date": "2024-04-19 21:07:10",
      "id": 1,
      "is_visible": true,
      "language_id": 1,
      "price": 1000,
      "title": "test python",
      "user_id": 1
    },
    {
      "about": "test java script about",
      "added_date": "2024-04-19 21:19:55",
      "id": 4,
      "is_visible": true,
      "language_id": 4,
      "price": 1000,
      "title": "test java script",
      "user_id": 2
    }
  ]
}
```
#### Получение одного проекта:
```text
GET https://URL/api/your_api_key/projects/1
```
Пример ответа:
```json
{
  "projects": {
    "about": "PROJECT ABOUT",
    "added_date": "2024-04-19 21:07:10",
    "id": 1,
    "is_visible": true,
    "language_id": 1,
    "price": 1000,
    "title": "PROJECT TITLE",
    "user_id": 1
  }
}
```
#### Добавление проекта:
```text
POST https://URL/api/your_api_key/projects
```
Добавление проектов через API не предусмотрено. Добавление только через интерфейс

Ответ:
```json
{"message": "Method Not Allowed"}
```
#### Редактирование проекта `PUT`:
При выполнении запроса `PUT` с неполным json неуказанные поля наменятся на `null`. Доступные поля для изменения запросом: `title`, `about`, `language_id`, `user_id`, `price`, `is_visible`
```text
PUT https://URL/api/your_api_key/projects/1
```
JSON:
```json
{
  "about": "PROJECT ABOUT NEW",
  "title": "PROJECT TITLE NEW"
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный проект:
```json
{
  "about": "PROJECT ABOUT NEW",
  "added_date": "2024-04-21 01:41:07",
  "id": 1,
  "is_visible": null,
  "language_id": null,
  "price": null,
  "title": "PROJECT TITLE NEW",
  "user_id": null
}
```
```text
PUT https://URL/api/your_api_key/projects/1
```
JSON:
```json
{
  "about": "PROJECT ABOUT NEW",
  "title": "PROJECT TITLE NEW",
  "is_visible": true,
  "language_id": 1,
  "price": 1000,
  "user_id": 1
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный проект:
```json
{
  "about": "PROJECT ABOUT NEW",
  "added_date": "2024-04-21 01:41:07",
  "id": 1,
  "is_visible": true,
  "language_id": 1,
  "price": 1000,
  "title": "PROJECT TITLE NEW",
  "user_id": 1
}
```
#### Редактирование пользователя `PATCH`:
При выполнении запроса `PATCH` с неполным json поменяются только те поля, которые были указаны. Доступные поля для изменения запросом: `title`, `about`, `language_id`, `user_id`, `price`, `is_visible`
```text
PATCH https://URL/api/your_api_key/projects/1
```
JSON:
```json
{
  "about": "PROJECT ABOUT NEW"
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный проект:
```json
{
  "about": "PROJECT ABOUT NEW",
  "added_date": "2024-04-21 01:41:07",
  "id": 1,
  "is_visible": true,
  "language_id": 1,
  "price": 1000,
  "title": "PROJECT TITLE",
  "user_id": 1
}
```

#### Удаления проекта:
```text
DELETE https://URL/api/your_api_key/projects/1
```
Ответ:
```json
{"success": "OK"}
```


### Работа с языками программирования
#### Получение всех языков программирования:
```text
GET https://URL/api/your_api_key/languages
```
Пример ответа:
```json
{
  "languages": [
    {
      "added_date": "2024-04-19 20:57:27",
      "id": 1,
      "language_sign": "Python",
      "language_title": "Python"
    },
    {
      "added_date": "2024-04-19 20:57:27",
      "id": 2,
      "language_sign": "Java",
      "language_title": "Java"
    },
    {
      "added_date": "2024-04-19 20:57:27",
      "id": 3,
      "language_sign": "C",
      "language_title": "С++"
    }
  ]
}
```
#### Получение одного языка программирования:
```text
GET https://URL/api/your_api_key/languages/1
```
Пример ответа:
```json
{
  "languages": {
    "added_date": "2024-04-19 20:57:27",
    "id": 1,
    "language_sign": "Python",
    "language_title": "Python"
  }
}
```
#### Добавление языка программирования:
```text
POST https://URL/api/your_api_key/languages
```
JSON
```json
{
  "language_title": "LANGUAGE TITLE",
  "language_sign": "LANGUAGE SIGN"
}
```
Ответ:
```json
{"success": "OK"}
```
#### Редактирование языка программирования `PUT`:
При выполнении запроса `PUT` с неполным json неуказанные поля наменятся на `null`. Доступные поля для изменения запросом: `language_title`, `language_sign`
* `language_title` - Название языка программирования
* `language_sign` - Написания языка программирования. Допустимые символы - все латинские буквы и дефис
```text
PUT https://URL/api/your_api_key/languages/1
```
JSON:
```json
{
  "language_title": "LANGUAGE TITLE NEW"
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный язык программирования:
```json
{
  "languages": {
    "added_date": "2024-04-19 20:57:27",
    "id": 1,
    "language_sign": null,
    "language_title": "LANGUAGE TITLE NEW"
  }
}
```
```text
PUT https://URL/api/your_api_key/languages/1
```
JSON:
```json
{
  "language_title": "LANGUAGE TITLE NEW",
  "language_sign": "LANGUAGE SIGN NEW"
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный язык программирования:
```json
{
  "languages": {
    "added_date": "2024-04-19 20:57:27",
    "id": 1,
    "language_sign": "LANGUAGE SIGN NEW",
    "language_title": "LANGUAGE TITLE NEW"
  }
}
```
#### Редактирование языка программирования `PATCH`:
При выполнении запроса `PATCH` с неполным json поменяются только те поля, которые были указаны. Доступные поля для изменения запросом: `language_title`, `language_sign`
* `language_title` - Название языка программирования
* `language_sign` - Написания языка программирования. Допустимые символы - все латинские буквы и дефис
```text
PATCH https://URL/api/your_api_key/languages/1
```
JSON:
```json
{
  "language_sign": "LANGUAGE SIGN NEW"
}
```
Ответ:
```json
{"success": "OK"}
```
Измененный язык программирования:
```json
{
  "languages": {
    "added_date": "2024-04-19 20:57:27",
    "id": 1,
    "language_sign": "LANGUAGE SIGN NEW",
    "language_title": "LANGUAGE TITLE"
  }
}
```

#### Удаления языка программирования:
```text
DELETE https://URL/api/your_api_key/languages/1
```
Ответ:
```json
{"success": "OK"}
```
