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
      "email": "ivan@test.com",
      "id": 1,
      "money": 1000,
      "name": "Ivan"
    }
}
```
#### Добавление пользователя:
```text
POST
```
Пример ответа:
```json
{'success': 'OK'}
```
#### Редактирование пользователя `PUT`:
При выполнении запроса `PUT` с неполным json неуказанные поля наменятся на `null` 
```text
PUT с полным запросом
```
Пример ответа:
```json
{'success': 'OK'}
```
Измененный пользователь:
```json
```
```text
PUT с неполным запросом
```
Пример ответа:
```json
{'success': 'OK'}
```
Измененный пользователь:
```json
```
#### Редактирование пользователя `PATCH`:
При выполнении запроса `PATCH` с неполным json поменяются только те поля, которые были указаны
```text
PATCH
```
Пример ответа:
```json
{'success': 'OK'}
```
Измененный пользователь:
```json
```
Пример ответа:
#### Удаления пользователя:
```text
DELETE
```
Пример ответа:
```json
{'success': 'OK'}
```
### Работа с проектами



### Работа с языками программирования

