# Created by Kelvin_Clark on 3/5/2022, 5:40 PM
from wtforms import Form, PasswordField, EmailField, validators


class SignInForm(Form):
    email = EmailField("Email", validators=[validators.input_required(), validators.email()],
                       render_kw={"placeholder": "Email"})
    password = PasswordField("Password", validators=[validators.input_required()],
                             render_kw={"placeholder": "Password"})
