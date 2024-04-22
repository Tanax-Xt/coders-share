import datetime

import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class ApiKey(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'api_keys'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    key = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)
    # api_keys_request = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('api_keys_requests.id'))
    added_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
