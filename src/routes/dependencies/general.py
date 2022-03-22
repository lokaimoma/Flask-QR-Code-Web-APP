# Created by Kelvin_Clark on 3/18/22, 4:53 PM
from src.utils.hex_to_rgb import hex_to_rgb


def __process_color_params(json: dict) -> dict:
    try:
        json["bg_color"] = hex_to_rgb(json["bg_color"])
    except KeyError:
        pass
    try:
        json["fg_color"] = hex_to_rgb(json["fg_color"])
    except KeyError:
        pass
    try:
        json["center_color"] = hex_to_rgb(json["center_color"])
    except KeyError:
        pass
    try:
        json["edge_color"] = hex_to_rgb(json["edge_color"])
    except KeyError:
        pass
    try:
        json["start_color"] = hex_to_rgb(json["start_color"])
    except KeyError:
        pass
    try:
        json["end_color"] = hex_to_rgb(json["end_color"])
    except KeyError:
        pass
    return json
