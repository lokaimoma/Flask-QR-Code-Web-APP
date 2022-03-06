# Created by Kelvin_Clark on 3/5/2022, 6:27 PM
from flask import Request
from flask.sessions import SessionMixin
from src.utils.security.password_util import verify_password_hash, hash_password
from src.dao.user import UserDao
from src.models.entities.user import User


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

    @staticmethod
    def register_user(request: Request, session: SessionMixin) -> bool:
        email = request.form["email"]
        if UserDao.check_user_exists(email=email):
            return False
        password = request.form["password"]
        username = request.form["username"]
        user = User(username=username, email=email, password=hash_password(password=password))
        UserDao.add_user(user=user)
        session["email"] = email
        session["username"] = user.username
        return True
