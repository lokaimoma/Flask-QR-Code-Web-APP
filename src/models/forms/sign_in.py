# Created by Kelvin_Clark on 3/5/2022, 5:40 PM
from wtforms import Form, PasswordField, EmailField, validators


class SignInForm(Form):
    email = EmailField("hello@mail.com", validators=[validators.input_required(), validators.email()])
    password = PasswordField("***********", validators=[validators.input_required()])
