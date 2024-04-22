import flask
from flask import redirect, url_for, render_template
from flask_login import login_required, logout_user, login_user, current_user

from data import db_session
from data.basket import Basket
from data.users import User
from forms.loginform import LoginForm
from forms.registerform import RegisterForm

blueprint = flask.Blueprint(
    'register_login_logout',
    __name__,
    template_folder='templates'
)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('projects.projects_list'))
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   form=form,
                                   message="Пользователь с таким email уже зарегистрирован")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()

        basket = Basket(user_id=user.id)
        db_sess.add(basket)
        db_sess.merge(user)
        db_sess.commit()
        login_user(user, remember=False)
        return redirect(url_for('projects.projects_list'))
    return render_template('register.html', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('projects.projects_list'))
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if not user:
            return render_template('login.html', message='Пользователь с такой почтой не зарегистрирован', form=form)
        if not user.check_password(form.password.data):
            return render_template('login.html', message='Пароль неверный', form=form)
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('projects.projects_list'))
    return render_template('login.html', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
