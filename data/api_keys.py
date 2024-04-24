import datetime

import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


# Модель для API-ключей
class ApiKey(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "api_keys"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    key = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)
    added_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
