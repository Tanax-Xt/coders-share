import os

from dotenv import load_dotenv
from flask import Flask, make_response, jsonify
from flask_login import LoginManager
from flask_restful import Api

from api.resources import languages_resource, users_resource, projects_resource
from blueprints import basket, register_login_logout, account, projects, main, developer, uploads
from data import db_session
from data.users import User

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
login_manager = LoginManager(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(403)
def forbidden(_):
    return make_response(jsonify({'error': 'Forbidden'}), 403)


@app.errorhandler(401)
def Unauthorized(_):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)


@app.errorhandler(500)
def InternalServerError(_):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    db_session.global_init("db/coders_share_database.db")

    app.register_blueprint(basket.blueprint)
    app.register_blueprint(register_login_logout.blueprint)
    app.register_blueprint(account.blueprint)
    app.register_blueprint(projects.blueprint)
    app.register_blueprint(main.blueprint)
    app.register_blueprint(developer.blueprint)
    app.register_blueprint(uploads.blueprint)

    api.add_resource(languages_resource.LanguagesListResource, '/api/<api_key>/languages')
    api.add_resource(languages_resource.LanguagesResource, '/api/<api_key>/languages/<int:id>')
    api.add_resource(users_resource.UsersListResource, '/api/<api_key>/users')
    api.add_resource(users_resource.UsersResource, '/api/<api_key>/users/<int:id>')
    api.add_resource(projects_resource.ProjectsListResource, '/api/<api_key>/projects')
    api.add_resource(projects_resource.ProjectsResource, '/api/<api_key>/projects/<int:id>')

    app.run(host, port)
