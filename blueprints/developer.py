import flask
from flask import render_template
from flask_login import login_required

from api.generate_api_key import get_api_key
from forms.developerform import DeveloperForm

blueprint = flask.Blueprint(
    'developer',
    __name__,
    template_folder='templates'
)


@blueprint.route('/developer', methods=['GET', 'POST'])
@login_required
def developer():
    form = DeveloperForm()
    if form.is_submitted():
        api_key = get_api_key()
        return render_template('developer.html', form=form, api_key=api_key)
    return render_template('developer.html', form=form)
