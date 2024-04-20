from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Length, NumberRange


class ReplenishmentForm(FlaskForm):
    sum = IntegerField("Сумма пополнения", validators=[DataRequired()], default=1000)
    num = StringField('Номер карты',
                      validators=[DataRequired(), Length(min=16, max=16, message='Длина номера карты – 16 символов')])
    month = IntegerField("Месяц", validators=[DataRequired(), NumberRange(min=1, max=12, message='Месяц от 1 до 12')])
    year = IntegerField("Год", validators=[DataRequired()])
    cvv = PasswordField('CVV', validators=[DataRequired(), Length(min=3, max=3, message='3 цифры')])
    submit = SubmitField('Пополнить')
