from flask_wtf import FlaskForm
from wtforms import EmailField, IntegerField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired(), NumberRange(min=1, max=120)])
    position = StringField("Должность", validators=[DataRequired()])
    speciality = StringField("Специальность", validators=[DataRequired()])
    address = StringField("Модуль проживания", validators=[DataRequired()])
    submit = SubmitField('Создать аккаунт')
