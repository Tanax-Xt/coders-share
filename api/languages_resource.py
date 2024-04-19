from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.api_keys import ApiKey
from data.languages import Language
from .parsers.languages_parser import parser_not_all_parameters, parser_all_parameters


class LanguagesResource(Resource):
    def get(self, api_key, language_id):
        abort_if_api_key_not_found(api_key)
        abort_if_language_not_found(language_id)
        session = db_session.create_session()
        language = session.query(Language).get(language_id)
        return jsonify({'languages': language.to_dict(only=('id', 'language_title', 'language_sign', 'added_date'))})

    def delete(self, api_key, language_id):
        abort_if_api_key_not_found(api_key)
        abort_if_language_not_found(language_id)
        session = db_session.create_session()
        language = session.query(Language).get(language_id)
        session.delete(language)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, api_key, language_id):
        abort_if_api_key_not_found(api_key)
        abort_if_language_not_found(language_id)
        args = parser_not_all_parameters.parse_args()
        session = db_session.create_session()
        language = session.query(Language).get(language_id)
        for key in filter(lambda x: args[x] is not None, args.keys()):
            setattr(language, key, args[key])
        session.commit()
        return jsonify({'success': 'OK'})


class LanguagesListResource(Resource):
    def get(self, api_key):
        abort_if_api_key_not_found(api_key)
        session = db_session.create_session()
        languages = session.query(Language).all()
        return jsonify({'languages': [item.to_dict(only=('id', 'language_title', 'language_sign', 'added_date')) for
                                      item in languages]})

    def post(self, api_key):
        abort_if_api_key_not_found(api_key)
        args = parser_all_parameters.parse_args()
        session = db_session.create_session()
        language = Language(
            language_title=args['language_title'],
            language_sign=args['language_sign'],
        )
        session.add(language)
        session.commit()
        return jsonify({'id': language.id})


def abort_if_api_key_not_found(api_key):
    session = db_session.create_session()
    api_key_db = session.query(ApiKey).filter(ApiKey.key == api_key).first()
    if not api_key_db:
        abort(403, message=f"Api key {api_key} not found")


def abort_if_language_not_found(language_id):
    session = db_session.create_session()
    language = session.query(Language).get(language_id)
    if not language:
        abort(404, message=f"Language {language_id} not found")
