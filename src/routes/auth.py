# Created by Kelvin_Clark on 3/4/2022, 3:40 PM
from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from src.models.forms.sign_in import SignInForm
from src.models.forms.sign_up import SignUpForm
from src.controllers.user import UserController
from src.utils.enum.flash_message_category import FlashMessageCategory

auth_router = Blueprint("auth", import_name=__name__)


@auth_router.route("/login/", methods=["GET", "POST"])
def login_route():
    form = SignInForm(formdata=request.form)
    if request.method == "POST" and form.validate():
        is_successful = UserController.login_user(request=request, session=session)
        if is_successful:
            return redirect(url_for("main.main_index"))
        flash(message="Incorrect Login Credentials or User doesn't exist", category=FlashMessageCategory.ERROR.value)
    return render_template("auth/signIn.html", form=form)


@auth_router.route("/register/", methods=["GET", "POST"])
def register_route():
    form = SignUpForm(formdata=request.form)
    if request.method == "POST" and form.validate():
        is_successful = UserController.register_user(request=request, session=session)
        if is_successful:
            return redirect(url_for("main.main_index"))
        flash(message="User might already exist. Try again with different credentials",
              category=FlashMessageCategory.WARNING.value)
    return render_template("auth/signUp.html", form=form)
