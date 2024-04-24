import flask
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from flask_restful import abort

from data import db_session
from data.basket import Basket
from data.projects import Project
from data.users import User
from forms.cardform import CardForm

blueprint = flask.Blueprint("basket", __name__, template_folder="templates")


# корзина, главная
@blueprint.route("/basket")
@login_required
def basket():
    try:
        db_sess = db_session.create_session()
        basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
        return render_template("basket.html", basket=basket)
    except Exception:
        return redirect(url_for("basket.basket"))


# корзина, добавление проекта
@blueprint.route("/basket/<int:id>", methods=["GET", "POST"])
@login_required
def add_project_to_basket(id):
    db_sess = db_session.create_session()
    project = db_sess.query(Project).filter(Project.id == id).first()
    basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
    if project:
        basket.projects.append(project)
        db_sess.commit()
        return redirect(url_for("basket.basket"))
    else:
        return abort(404)


# корзина, удаление проекта
@blueprint.route("/basket_delete/<int:id>", methods=["GET", "POST"])
@login_required
def del_project_from_basket(id):
    db_sess = db_session.create_session()
    project = db_sess.query(Project).filter(Project.id == id).first()
    basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
    if project:
        basket.projects.remove(project)
        db_sess.commit()
        return redirect(url_for("basket.basket"))
    else:
        return abort(404)


# корзина, оформление заказа
@blueprint.route("/basket/buy", methods=["GET", "POST"])
@login_required
def basket_buy():
    try:
        db_sess = db_session.create_session()
        basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
        form = CardForm()
        if form.validate_on_submit():
            return basket_complete(from_card=True)
        return render_template("buy.html", basket=basket, form=form)
    except Exception:
        return redirect(url_for("basket.basket"))


# корзина, покупку
@blueprint.route("/basket/buy/complete")
@login_required
def basket_complete(from_card=False):
    try:
        db_sess = db_session.create_session()
        basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        sm = 0
        for proj in basket.projects:
            owner = db_sess.query(User).filter(User.id == proj.user_id).first()
            owner.money += proj.price
            db_sess.commit()
            user.bought_projects.append(proj)
            basket.projects.remove(proj)
            sm += proj.price
        db_sess.commit()
        if not from_card:
            user.money -= sm
            db_sess.commit()
        return render_template("completed_payment.html")
    except Exception:
        return redirect(url_for("basket.basket"))
