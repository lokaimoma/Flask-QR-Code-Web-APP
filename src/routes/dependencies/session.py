# Created by Kelvin_Clark on 3/10/22, 1:16 PM
from flask import session, redirect, Response, url_for
from functools import wraps
from typing import Callable, Union, Any

from src.exceptions import UserDoesNotExist
from src.dao.user import UserDao


def login_required(callback: Callable) -> Union[Any, Response]:
    @wraps(callback)
    def wrap(*args, **kwargs):
        try:
            email = session["email"]
            if not UserDao.check_user_exists(email=email):
                raise UserDoesNotExist()
            return callback(*args, **kwargs)
        except (KeyError, UserDoesNotExist):
            return redirect(url_for("auth.login"))
    return wrap
