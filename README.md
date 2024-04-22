# Coders Share 
![last commit](https://img.shields.io/github/last-commit/Tanax-Xt/coders-share) ![license](https://img.shields.io/github/license/Tanax-Xt/coders-share)

Coders Share – это онлайн-площадка для покупки и продажи проектов и их частей

Воспользоваться сервисом можно по ссылке [coders-share-yandexhack.amvera.io](https://coders-share-yandexhack.amvera.io/)


#### Содержание
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

#### Содержание
  <ol>
    <li><a href="#получение-ключа">Получение ключа</a></li>
    <li><a href="#работа-с-API-ключом">Работа с API-ключом</a></li>
    <li><a href="#работа-с-пользователями">Работа с пользователями</a></li>
    <li><a href="#работа-с-проектами">Работа с проектами</a></li>
    <li><a href="#работа-с-языками-программирования">Работа с языками программирования</a></li>
  </ol>

#### Получение ключа
Для получения API-ключа зарегистрируйтесь на сайте и перейдите на страницу `/developer`. Нажмите на кнопку для генерации ключа. Вы получите ключ доступа к API, состоящий из 32 символов 


#### Работа с API-ключом
После получения API-ключа вы можете обращаться к API по следующей схеме:

`https://coders-share-yandexhack.amvera.io/api/your_api_key/data_category`
* `your_api_key` - ваш API-ключ
* `data_category` - необходима категория данных


#### Работа с пользователями



#### Работа с проектами



#### Работа с языками программирования

