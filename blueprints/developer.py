import flask
from flask import render_template, redirect, url_for
from flask_login import current_user

from api.generate_api_key import get_api_key
from forms.developerform import DeveloperForm

blueprint = flask.Blueprint("developer", __name__, template_folder="templates")

# генерация API-ключа
@blueprint.route("/developer", methods=["GET", "POST"])
def developer():
    try:
        if current_user.is_authenticated:
            form = DeveloperForm()
            if form.is_submitted():
                api_key = get_api_key()
                return render_template("developer.html", form=form, api_key=api_key)
            return render_template("developer.html", form=form)
        return render_template("developer.html")
    except Exception:
        return redirect(url_for("developer.developer"))
