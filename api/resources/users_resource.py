from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.api_keys import ApiKey
from data.basket import Basket
from data.users import User
from api.parsers.users_parser import parser_not_all_parameters, parser_all_parameters


class UsersResource(Resource):
    def get(self, api_key, id):
        abort_if_api_key_not_found(api_key)
        abort_if_user_not_found(id)
        session = db_session.create_session()
        user = session.query(User).get(id)
        return jsonify(
            {"users": user.to_dict(only=("id", "email", "name", "added_date", "money"))}
        )

    def delete(self, api_key, id):
        abort_if_api_key_not_found(api_key)
        abort_if_user_not_found(id)
        session = db_session.create_session()
        user = session.query(User).get(id)
        session.delete(user)
        session.commit()
        return jsonify({"success": "OK"})

    def put(self, api_key, id):
        abort_if_api_key_not_found(api_key)
        abort_if_user_not_found(id)
        args = parser_not_all_parameters.parse_args()
        session = db_session.create_session()
        user = session.query(User).get(id)
        for key in args.keys():
            setattr(user, key, args[key])
        session.commit()
        return jsonify({"success": "OK"})

    def patch(self, api_key, id):
        abort_if_api_key_not_found(api_key)
        abort_if_user_not_found(id)
        args = parser_not_all_parameters.parse_args()
        session = db_session.create_session()
        user = session.query(User).get(id)
        for key in filter(lambda x: args[x] is not None, args.keys()):
            setattr(user, key, args[key])
        session.commit()
        return jsonify({"success": "OK"})


class UsersListResource(Resource):
    def get(self, api_key):
        abort_if_api_key_not_found(api_key)
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify(
            {
                "users": [
                    item.to_dict(only=("id", "email", "name", "added_date", "money"))
                    for item in users
                ]
            }
        )

    def post(self, api_key):
        abort_if_api_key_not_found(api_key)
        args = parser_all_parameters.parse_args()
        session = db_session.create_session()
        if session.query(User).filter(User.email == args["email"]).first():
            return abort(409, message="Account already exists")
        user = User(name=args["name"], email=args["email"])
        user.set_password(args["password"])
        session.add(user)
        session.commit()

        basket = Basket(user_id=user.id)
        session.add(basket)
        session.merge(user)
        session.commit()

        return jsonify({"id": user.id})


def abort_if_api_key_not_found(api_key):
    session = db_session.create_session()
    api_key_db = session.query(ApiKey).filter(ApiKey.key == api_key).first()
    if not api_key_db:
        abort(403, message=f"Api key {api_key} not found")


def abort_if_user_not_found(id):
    session = db_session.create_session()
    user = session.query(User).get(id)
    if not user:
        abort(404, message=f"User {id} not found")
