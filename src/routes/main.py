# Created by Kelvin_Clark on 3/10/22, 1:10 PM
from flask import Blueprint, session, redirect, render_template
from .dependencies.session import login_required

main_router = Blueprint("main", import_name=__name__)


@main_router.route("/")
@login_required
def main_index():
    return render_template("main/index.html")
