# Created by Kelvin_Clark on 3/5/2022, 6:27 PM
from flask import Request
from flask.sessions import SessionMixin
from src.utils.security.password_util import verify_password_hash
from src.dao.user import UserDao


class UserController:

    @staticmethod
    def login_user(request: Request, session: SessionMixin) -> bool:
        email = request.form["email"]
        password = request.form["password"]
        user = UserDao.get_user_by_email(email=email)
        if user is None:
            return False
        if not verify_password_hash(password=password, password_hash=user.password):
            return False
        session["email"] = email
        session["username"] = user.username
        return True
