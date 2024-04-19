import sqlalchemy
from sqlalchemy.util.preloaded import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase



class Basket(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'basket'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))

    # user = orm.relationship('User')
    user = orm.relationship("User", back_populates='basket')

    projects = orm.relationship("Project",
                               secondary="basket_to_projects",
                               backref="basket")
