import flask
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from data import db_session
from data.projects import Project
from data.users import User
from forms.replenishmentform import ReplenishmentForm
from forms.withdrawalform import WithdrawalForm

blueprint = flask.Blueprint("account", __name__, template_folder="templates")


# личный кабинет, главная страница
@blueprint.route("/account", methods=["GET", "POST"])
@login_required
def account():
    try:
        db_sess = db_session.create_session()
        owner_projects = (
            db_sess.query(Project).filter(Project.user == current_user).all()
        )
        return render_template("account.html", owner_projects=owner_projects)
    except Exception:
        return redirect(url_for("account.account"))


# личный кабинет, пополнение счета
@blueprint.route("/account/replenishment", methods=["GET", "POST"])
@login_required
def account_replenishment():
    form = ReplenishmentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        user.money += form.sum.data
        db_sess.commit()
        return redirect(url_for("account.account"))
    return render_template("replenishment.html", form=form)


# личный кабинет, вывод средств
@blueprint.route("/account/withdrawal", methods=["GET", "POST"])
@login_required
def account_withdrawal():
    form = WithdrawalForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        user.money = 0
        db_sess.commit()
        return redirect(url_for("account.account"))
    return render_template("withdrawal.html", form=form)
