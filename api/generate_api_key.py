import secrets

from data import db_session, api_keys

# Генерация API-ключей
def get_api_key():
    api_key = secrets.token_hex(nbytes=16)
    key = api_keys.ApiKey(key=api_key)

    session = db_session.create_session()
    session.add(key)
    session.commit()

    return key.key


if __name__ == "__main__":
    db_session.global_init("db/coders_share_database.db")
    print(get_api_key())
