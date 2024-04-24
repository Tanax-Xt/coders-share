import flask
from flask import render_template

blueprint = flask.Blueprint("main", __name__, template_folder="templates")


# Главная
@blueprint.route("/")
def main():
    return render_template("main.html")
