# Created by Kelvin_Clark on 3/5/2022, 5:40 PM
from wtforms import Form, PasswordField, EmailField, validators


class SignInForm(Form):
    email = EmailField("Email", validators=[validators.input_required(), validators.email()])
    password = PasswordField("Password", validators=[validators.input_required()])
