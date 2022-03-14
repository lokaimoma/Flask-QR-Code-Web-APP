# Created by Kelvin_Clark on 3/13/22, 7:49 PM
from enum import Enum


class QRDrawerShapeEnum(str, Enum):
    SQUARED = "squared"
    GAPED_SQUARED = "gaped_squared"
    CIRCLE = "circle"
    ROUND = "round"
    HORIZONTAL_BAR = "horizontal_bar"
    VERTICAL_BAR = "vertical_bar"


class QRColorMode(str, Enum):
    SOLID = "solid"
    RADIAL = "radial"
    SQUARE = "square"
    LINEAR = "linear"
    LINEAR_HORIZONTAL = "linear_horizontal"
    LINEAR_VERTICAL = "linear_vertical"
