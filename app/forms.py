from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired


class BasicForm(FlaskForm):
    nombre = StringField('Nombre')
    apellido = StringField('Apellido')
    submit = SubmitField('Enviar')


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Ingresar")


class RegisterForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    sobre_mi = StringField("Sobre mi", validators=[DataRequired()])
    submit = SubmitField("Crear cuenta")
