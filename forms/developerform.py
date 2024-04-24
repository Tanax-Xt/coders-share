from flask_wtf import FlaskForm
from wtforms import SubmitField


# форма, получения API-ключа
class DeveloperForm(FlaskForm):
    submit = SubmitField("Получить API-ключ")
