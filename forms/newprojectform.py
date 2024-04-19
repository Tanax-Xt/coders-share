from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

from data import db_session

languages_list = None


class NewProjectForm(FlaskForm):
    name = StringField('Название проекта', validators=[DataRequired()])
    about = StringField('Описание проекта', validators=[DataRequired()], widget=TextArea())
    banner = FileField('Баннер (будет отображаться при просмотре карточки проекта). Тип файла: jpg/png',
                       validators=[
                           FileRequired(),
                           FileAllowed(['jpg', 'png'], 'Images only!')
                       ])

    db_session.global_init('db/coders_share_database.db')
    sess = db_session.create_session()

    language = SelectField('Язык проекта', choices=languages_list)
    files = FileField('zip-архив с файлами проекта', validators=[FileRequired()])
    price = IntegerField('Цена доступа в рублях', validators=[DataRequired()], default=1000)
    accept_lang = BooleanField('Подтверждаю корректность выбранного языка', validators=[DataRequired()])
    accept_file = BooleanField('Подтверждаю корректность загруженных файлов', validators=[DataRequired()])
    submit = SubmitField('Добавить проект')
