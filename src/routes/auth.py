# Created by Kelvin_Clark on 3/4/2022, 3:40 PM
from flask import Blueprint, render_template, request, session, flash
from src.models.forms.sign_in import SignInForm
from src.controllers.user import UserController

auth_router = Blueprint("auth", import_name=__name__)


@auth_router.route("/login", methods=["GET", "POST"])
def login_route():
    form = SignInForm(formdata=request.form)
    if request.method == "POST":
        is_successful = UserController.login_user(request=request, session=session)
        if is_successful:
            pass
            # TODO: Redirect to qr code page / user page (Not sure yet)
        flash(message="Incorrect Login Credentials or User doesn't exist")
    return render_template("auth/signIn.html", form=form)
