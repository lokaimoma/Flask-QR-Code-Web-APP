# Created by Kelvin_Clark on 3/6/2022, 7:08 PM
from wtforms import PasswordField, StringField, validators
from .sign_in import SignInForm


class SignUpForm(SignInForm):
    confirm_password = PasswordField("Confirm password",
                                     validators=[validators.input_required(),
                                                 validators.EqualTo(fieldname="password",
                                                                    message="Passwords don't match")
                                                 ],
                                     render_kw={"placeholder": "Confirm password"})
    username = StringField(label="Username", validators=[validators.input_required()],
                           render_kw={"placeholder": "Username"})
