import os

import flask
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from flask_restful import abort

from data import db_session
from data.basket import Basket
from data.languages import Language
from data.projects import Project
from forms.newprojectform import NewProjectForm

blueprint = flask.Blueprint("projects", __name__, template_folder="templates")


# Проекты, главная
@blueprint.route("/projects")
def projects_list():
    try:
        sess = db_session.create_session()
        languages = sess.query(Language).all()
        projects = sess.query(Project).filter(Project.is_visible == True).all()
        if current_user.is_authenticated:
            basket = sess.query(Basket).filter(Basket.user == current_user).first()
            return render_template("projects.html", languages=languages, projects=projects, basket=basket)
        return render_template("projects.html", languages=languages, projects=projects, basket=[])
    except Exception:
        return redirect(url_for("projects.projects_list"))


# Проекты, добавление
@blueprint.route("/projects/add", methods=["GET", "POST"])
@login_required
def add_project():
    db_sess = db_session.create_session()
    languages = db_sess.query(Language).all()
    languages_list = [(f"{i + 1}", lang.language_title) for i, lang in enumerate(languages)]

    form = NewProjectForm()
    form.language.choices = languages_list
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        project = Project(
            title=form.name.data,
            about=form.about.data,
            language_id=db_sess.query(Language).all()[int(form.language.data) - 1].id,
            user_id=current_user.id,
            price=form.price.data
        )
        db_sess.add(project)
        db_sess.commit()
        directory = f"static/users_data/{current_user.id}/{project.id}"
        if not os.path.exists(directory):
            os.makedirs(directory)
        form.banner.data.save(f"{directory}/banner.jpg")
        form.files.data.save(f"{directory}/files.zip")
        project.banner = directory + "/banner.jpg"
        project.files = directory + "/files.zip"
        db_sess.commit()
        return redirect(url_for("projects.projects_list"))
    return render_template("create_project.html", form=form)


# Проекты, удаление
@blueprint.route("/projects_delete/<int:id>", methods=["GET", "POST"])
@login_required
def projects_delete(id):
    db_sess = db_session.create_session()
    project = (db_sess.query(Project).filter(Project.id == id, Project.user == current_user).first())
    if project:
        project.is_visible = False
        db_sess.commit()
    else:
        return abort(404)
    return redirect(url_for("projects.projects_list"))
