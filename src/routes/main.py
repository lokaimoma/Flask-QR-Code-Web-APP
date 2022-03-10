# Created by Kelvin_Clark on 3/10/22, 1:10 PM
from flask import Blueprint, session, redirect


main_router = Blueprint("main", import_name=__name__)

@main_router.route("/")
def main_index():

