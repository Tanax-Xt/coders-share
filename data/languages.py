import datetime

import sqlalchemy
from sqlalchemy.util.preloaded import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


# Модель для ЯП
class Language(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "languages"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    language_title = sqlalchemy.Column(sqlalchemy.String)
    language_sign = sqlalchemy.Column(sqlalchemy.String)
    added_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    projects = orm.relationship("Project", back_populates="language")
