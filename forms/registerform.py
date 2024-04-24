from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length


# форма, регистрация
class RegisterForm(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired()])
    password = PasswordField(
        "Пароль",
        validators=[DataRequired(), Length(min=8, message="Минимум 8 символов")]
    )
    password_again = PasswordField("Повторите пароль", validators=[DataRequired()])
    name = StringField("Имя пользователя", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")
