import flask
from flask import send_from_directory
from flask_login import login_required, current_user
from flask_restful import abort

blueprint = flask.Blueprint(
    'uploads',
    __name__,
    template_folder='templates'
)


@blueprint.route('/uploads/<path:filename>', methods=['GET', 'POST'])
@login_required
def download(filename):
    if current_user.is_authenticated and (
            (current_user.id == int(filename.split('/')[0])) or any(int(filename.split('/')[1]) == proj.id for proj in
                                                                    current_user.bought_projects)):
        uploads = 'static/users_data'
        return send_from_directory(uploads, filename)
    return abort(403)
