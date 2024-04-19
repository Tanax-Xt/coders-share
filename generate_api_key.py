from hashlib import md5
from random import randint

from data import db_session, api_keys


def get_api_key():
    pas = ''.join([f'{chr(randint(65, 122))}{randint(-10 ** 9, 10 ** 9)}' for i in range(20)])
    key = api_keys.ApiKey(key=md5(pas.encode()).hexdigest())

    db_session.global_init('db/coders_share_database.db')
    session = db_session.create_session()
    session.add(key)
    session.commit()

    return key.key


if __name__ == '__main__':
    print(get_api_key())
