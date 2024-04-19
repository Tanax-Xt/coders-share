import datetime

import sqlalchemy
from flask_login import UserMixin
from sqlalchemy.util.preloaded import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase

association_table = sqlalchemy.Table(
    'bought_projects_to_user',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('projects', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('projects.id')),
    sqlalchemy.Column('users', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'))
)

association_table_2 = sqlalchemy.Table(
    'basket_to_projects',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('basket', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('basket.id')),
    sqlalchemy.Column('projects', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('projects.id'))

)


class Project(SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'projects'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    about = sqlalchemy.Column(sqlalchemy.String)
    banner = sqlalchemy.Column(sqlalchemy.String)
    language_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('languages.id'))
    files = sqlalchemy.Column(sqlalchemy.String)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    price = sqlalchemy.Column(sqlalchemy.Integer)
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    added_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    user = orm.relationship('User')
    language = orm.relationship('Language')


