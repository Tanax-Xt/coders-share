import datetime

import sqlalchemy
from flask_login import UserMixin
from sqlalchemy.util.preloaded import orm
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    added_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)

    projects = orm.relationship("Project", back_populates='user')

    basket = orm.relationship('Basket')
    # basket = orm.relationship("Basket", back_populates='user')

    bought_projects = orm.relationship("Project",
                                       secondary="bought_projects_to_user",
                                       backref="users")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

# добавить привязку всех проектов пользователя
