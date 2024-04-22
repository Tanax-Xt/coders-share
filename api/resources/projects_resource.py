from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.api_keys import ApiKey
from data.projects import Project
from api.parsers.projects_parser import parser_not_all_parameters


class ProjectsResource(Resource):
    def get(self, api_key, id):
        abort_if_api_key_not_found(api_key)
        abort_if_project_not_found(id)
        session = db_session.create_session()
        projects = session.query(Project).get(id)
        return jsonify({'projects': projects.to_dict(
            only=('id', 'title', 'about', 'language_id', 'user_id', 'price', 'is_visible', 'added_date'))})

    def delete(self, api_key, id):
        abort_if_api_key_not_found(api_key)
        abort_if_project_not_found(id)
        session = db_session.create_session()
        project = session.query(Project).get(id)
        project.is_visible = False
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, api_key, id):
        abort_if_api_key_not_found(api_key)
        abort_if_project_not_found(id)
        args = parser_not_all_parameters.parse_args()
        session = db_session.create_session()
        project = session.query(Project).get(id)
        for key in args.keys():
            setattr(project, key, args[key])
        session.commit()
        return jsonify({'success': 'OK'})

    def patch(self, api_key, id):
        abort_if_api_key_not_found(api_key)
        abort_if_project_not_found(id)
        args = parser_not_all_parameters.parse_args()
        session = db_session.create_session()
        project = session.query(Project).get(id)
        for key in filter(lambda x: args[x] is not None, args.keys()):
            setattr(project, key, args[key])
        session.commit()
        return jsonify({'success': 'OK'})


class ProjectsListResource(Resource):
    def get(self, api_key):
        abort_if_api_key_not_found(api_key)
        session = db_session.create_session()
        users = session.query(Project).all()
        return jsonify({'projects': [
            item.to_dict(only=('id', 'title', 'about', 'language_id', 'user_id', 'price', 'is_visible', 'added_date'))
            for item in users]})

    def post(self, api_key):
        # добавление проектов только через интерфейс
        abort(405, message='Method Not Allowed')


def abort_if_api_key_not_found(api_key):
    session = db_session.create_session()
    api_key_db = session.query(ApiKey).filter(ApiKey.key == api_key).first()
    if not api_key_db:
        abort(403, message=f"Api key {api_key} not found")


def abort_if_project_not_found(id):
    session = db_session.create_session()
    project = session.query(Project).get(id)
    if not project:
        abort(404, message=f"Project {id} not found")
