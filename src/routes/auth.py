# Created by Kelvin_Clark on 3/4/2022, 3:40 PM
from flask import Blueprint, render_template, request

auth_router = Blueprint("auth", import_name=__name__)


@auth_router.route("/login", methods=["GET", "POST"])
def login_route():
    if request.method == "GET":
        return render_template("auth/signIn.html")
    # TODO: Handle POST Request
