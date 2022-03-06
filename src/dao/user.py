# Created by Kelvin_Clark on 3/5/2022, 6:37 PM
from typing import Optional

from src.models.entities.user import User
from src import database as db


class UserDao:

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def check_user_exists(email: str) -> bool:
        """
        True if user exits, False if otherwise
        :param email: str
        :return: bool
        """
        user = UserDao.get_user_by_email(email=email)
        return user is not None

    @staticmethod
    def add_user(user: User) -> User:
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return user
