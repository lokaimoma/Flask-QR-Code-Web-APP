# Created by Kelvin_Clark on 3/10/22, 1:37 PM
class AppException(Exception):
    def __init__(self, message: str):
        self.message = message


class UserDoesNotExist(AppException):
    def __init__(self):
        super(UserDoesNotExist, self).__init__(message="No user found with provided credential(s)")
