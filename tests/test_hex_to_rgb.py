# Created by Kelvin_Clark on 3/14/22, 6:46 PM
import pytest
from src.utils.hex_to_rgb import hex_to_rgb


@pytest.mark.parametrize(argnames=["hex_", "rgb"],
                         argvalues=[
                             ("", (0, 0, 0)),
                             (" ", (0, 0, 0)),
                             ("#0040a5", (0, 64, 165)),
                             ("#800000", (128, 0, 0)),
                             ("#fff", (255, 255, 255)),
                             ("#80000044", (128, 0, 0))
                         ])
def test_hex_to_rgb(hex_, rgb):
    result = hex_to_rgb(hex_code=hex_)
    assert result == rgb
