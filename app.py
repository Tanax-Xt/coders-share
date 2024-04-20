import os

from dotenv import load_dotenv
from flask import Flask, make_response, jsonify, render_template, redirect, url_for, send_from_directory
from flask_login import login_user, LoginManager, current_user, login_required, logout_user
from flask_restful import Api, abort

from api import languages_resource
from data import db_session
from data.basket import Basket
from data.languages import Language
from data.projects import Project
from data.users import User
from forms.cardform import CardForm
from forms.loginform import LoginForm
from forms.newprojectform import NewProjectForm
from forms.registerform import RegisterForm
from forms.replenishmentform import ReplenishmentForm
from forms.withdrawalform import WithdrawalForm

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
login_manager = LoginManager(app)
login_manager.init_app(app)

@app.route('/account/withdrawal', methods=['GET', 'POST'])
@login_required
def account_withdrawal():
    form = WithdrawalForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        user.money = 0
        db_sess.commit()
        return redirect(url_for('account'))
    return render_template('withdrawal.html', form=form)



@app.route('/account/replenishment', methods=['GET', 'POST'])
@login_required
def account_replenishment():
    form = ReplenishmentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        user.money += form.sum.data
        db_sess.commit()
        return redirect(url_for('account'))
    return render_template('replenishment.html', form=form)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    try:
        db_sess = db_session.create_session()
        owner_projects = db_sess.query(Project).filter(Project.user == current_user).all()
        return render_template('account.html', owner_projects=owner_projects)
    except Exception:
        return redirect(url_for('account'))


@app.route('/basket/buy/complete')
@login_required
def basket_complete(from_card=False):
    try:
        db_sess = db_session.create_session()
        basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        sm = 0
        for proj in basket.projects:
            user.bought_projects.append(proj)
            basket.projects.remove(proj)
            sm += proj.price
        db_sess.commit()
        if not from_card:
            user.money -= sm
        db_sess.commit()
        return render_template('completed_payment.html')
    except Exception:
        return redirect(url_for('basket'))


@app.route('/basket/buy', methods=['GET', 'POST'])
@login_required
def basket_buy():
    try:
        db_sess = db_session.create_session()
        basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
        form = CardForm()
        if form.validate_on_submit():
            return basket_complete(from_card=True)
        return render_template('buy.html', basket=basket, form=form)
    except Exception:
        return redirect(url_for('basket'))


@app.route('/basket_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def del_project_from_basket(id):
    db_sess = db_session.create_session()
    project = db_sess.query(Project).filter(Project.id == id).first()
    basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
    if project:
        basket.projects.remove(project)
        db_sess.commit()
        return redirect(url_for('basket'))
    else:
        return abort(404)


@app.route('/basket/<int:id>', methods=['GET', 'POST'])
@login_required
def add_project_to_basket(id):
    db_sess = db_session.create_session()
    project = db_sess.query(Project).filter(Project.id == id).first()
    basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
    if project:
        basket.projects.append(project)
        db_sess.commit()
        return redirect(url_for('basket'))
    else:
        return abort(404)


@app.route('/basket')
@login_required
def basket():
    try:
        db_sess = db_session.create_session()
        basket = db_sess.query(Basket).filter(Basket.user_id == current_user.id).first()
        return render_template('basket.html', basket=basket)
    except Exception:
        return redirect(url_for('basket'))


@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
@login_required
def download(filename):
    if current_user.is_authenticated and (
            (current_user.id == int(filename.split('/')[0])) or any(int(filename.split('/')[1]) == proj.id for proj in
                                                                    current_user.bought_projects)):
        uploads = 'static/users_data'
        return send_from_directory(uploads, filename)
    return abort(403)


@app.route('/projects_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def projects_delete(id):
    db_sess = db_session.create_session()
    project = db_sess.query(Project).filter(Project.id == id, Project.user == current_user).first()
    if project:
        project.is_visible = False
        db_sess.commit()
    else:
        not_found('')
    return redirect(url_for('projects'))


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


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/projects/add', methods=['GET', 'POST'])
def add_project():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    db_sess = db_session.create_session()
    languages = db_sess.query(Language).all()
    languages_list = [(f'{i + 1}', lang.language_title) for i, lang in enumerate(languages)]

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
        directory = f'static/users_data/{current_user.id}/{project.id}'
        if not os.path.exists(directory):
            os.makedirs(directory)
        form.banner.data.save(f'{directory}/banner.jpg')
        form.files.data.save(f'{directory}/files.zip')
        project.banner = directory + '/banner.jpg'
        project.files = directory + '/files.zip'
        db_sess.commit()
        return redirect(url_for('projects'))
    return render_template('create_project.html', form=form)


@app.route('/projects')
def projects():
    try:
        sess = db_session.create_session()
        languages = sess.query(Language).all()
        projects = sess.query(Project).filter(Project.is_visible == True).all()
        if current_user.is_authenticated:
            basket = sess.query(Basket).filter(Basket.user == current_user).first()
            return render_template('projects.html', languages=languages, projects=projects, basket=basket)
        return render_template('projects.html', languages=languages, projects=projects, basket=[])
    except Exception:
        return redirect(url_for('projects'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('projects'))
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
            return redirect(url_for('projects'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('projects'))
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
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()

        basket = Basket(user_id=user.id)
        db_sess.add(basket)
        db_sess.merge(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    db_session.global_init("db/coders_share_database.db")
    api.add_resource(languages_resource.LanguagesListResource, '/api/<api_key>/languages')
    api.add_resource(languages_resource.LanguagesResource, '/api/<api_key>/languages/<int:language_id>')
    # добавить апи для пользователей
    # добавить апи для projects
    app.run(host, port)
