# Created by Kelvin_Clark on 3/13/22, 6:25 PM
from typing import Union, Any, Optional

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.pil import PilImage
from qrcode.image.styles.moduledrawers import (
    QRModuleDrawer, SquareModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer,
    RoundedModuleDrawer, HorizontalBarsDrawer, VerticalBarsDrawer
)
from qrcode.image.styles.colormasks import (QRColorMask, SolidFillColorMask, SquareGradiantColorMask,
                                            RadialGradiantColorMask, HorizontalGradiantColorMask,
                                            VerticalGradiantColorMask)

from .enums import QRDrawerShapeEnum, QRColorMode


def generate_qr_code_image(data: Any, shape: str, color_mode: str, **kwargs) -> Union[PilImage, Any]:
    qr = qrcode.QRCode()
    qr.add_data(data)
    s = __get_shape_module(shape)
    if not s:
        return qr.make_image()
    color_mode = color_mode.lower()
    m: QRColorMask
    if color_mode == QRColorMode.RADIAL.value:
        m = __get_radial_gradient_clr_mask(**kwargs)
    elif color_mode == QRColorMode.SQUARE.value:
        m = __get_square_gradient_clr_mask(**kwargs)
    elif color_mode == QRColorMode.LINEAR.value:
        m = __get_linear_gradient_clr_mask(**kwargs)
    else:
        m = __get_solid_clr_mask(**kwargs)
    return qr.make_image(image_factory=StyledPilImage, color_mask=m, module_drawer=s)


def __get_shape_module(shape: str) -> Optional[QRModuleDrawer]:
    shape = shape.lower()
    if shape == QRDrawerShapeEnum.SQUARED.value:
        return SquareModuleDrawer()
    elif shape == QRDrawerShapeEnum.GAPED_SQUARED.value:
        return GappedSquareModuleDrawer()
    elif shape == QRDrawerShapeEnum.CIRCLE.value:
        return CircleModuleDrawer()
    elif shape == QRDrawerShapeEnum.ROUND.value:
        return RoundedModuleDrawer()
    elif shape == QRDrawerShapeEnum.HORIZONTAL_BAR.value:
        return HorizontalBarsDrawer()
    elif shape == QRDrawerShapeEnum.VERTICAL_BAR.value:
        return VerticalBarsDrawer()
    else:
        return None


def __get_solid_clr_mask(bg_color: tuple[int, int, int] = (255, 255, 255),
                         fg_color: tuple[int, int, int] = (0, 0, 0)) -> SolidFillColorMask:
    return SolidFillColorMask(back_color=bg_color, front_color=fg_color)


def __get_square_gradient_clr_mask(bg_color: tuple[int, int, int] = (255, 255, 255),
                                   center_color: tuple[int, int, int] = (0, 0, 0),
                                   edge_color: tuple[int, int, int] = (0, 0, 255)) -> SquareGradiantColorMask:
    return SquareGradiantColorMask(back_color=bg_color, center_color=center_color, edge_color=edge_color)


def __get_radial_gradient_clr_mask(bg_color: tuple[int, int, int] = (255, 255, 255),
                                   center_color: tuple[int, int, int] = (0, 0, 0),
                                   edge_color: tuple[int, int, int] = (0, 0, 255)) -> RadialGradiantColorMask:
    return RadialGradiantColorMask(back_color=bg_color, center_color=center_color, edge_color=edge_color)


def __get_linear_gradient_clr_mask(direction: str, bg_color: tuple[int, int, int] = (255, 255, 255),
                                   start_color: tuple[int, int, int] = (0, 0, 0),
                                   end_color: tuple[int, int, int] = (0, 0, 255), ) -> \
        Union[HorizontalGradiantColorMask, VerticalGradiantColorMask]:
    direction = direction.lower()
    if direction == QRColorMode.LINEAR_VERTICAL:
        return VerticalGradiantColorMask(back_color=bg_color, top_color=start_color, bottom_color=end_color)
    else:
        return HorizontalGradiantColorMask(back_color=bg_color, left_color=start_color, right_color=end_color)
