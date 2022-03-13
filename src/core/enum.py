# Created by Kelvin_Clark on 3/13/22, 7:49 PM
from enum import Enum


class QRDrawerShape(str, Enum):
    SQUARED = "squared"
    GAPED_SQUARED = "gaped-squared"
    CIRCLE = "circle"
    ROUND = "round"
    HORIZONTAL_BAR = "horizontal_bar"
    VERTICAL_BAR = "vertical_bar"
