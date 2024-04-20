from flask_wtf import FlaskForm
from wtforms import SubmitField


class DeveloperForm(FlaskForm):
    submit = SubmitField('Получить API-ключ')
