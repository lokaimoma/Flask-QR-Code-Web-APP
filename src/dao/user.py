# Created by Kelvin_Clark on 3/5/2022, 6:37 PM
from typing import Optional

from src.models.entities.user import User


class UserDao:

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        return User.query.filter_by(email=email).first()
