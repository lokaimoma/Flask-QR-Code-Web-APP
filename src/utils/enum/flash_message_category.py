# Created by Kelvin_Clark on 3/5/2022, 7:35 PM
from enum import Enum


class FlashMessageCategory(str, Enum):
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
