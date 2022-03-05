# Created by Kelvin_Clark on 3/4/2022, 3:40 PM
from flask import Blueprint, render_template, request
from src.models.forms.sign_in import SignInForm

auth_router = Blueprint("auth", import_name=__name__)


@auth_router.route("/login", methods=["GET", "POST"])
def login_route():
    form = SignInForm(formdata=request.form)
    if request.method == "GET":
        return render_template("auth/signIn.html", form=form)
    # TODO: Handle POST Request
