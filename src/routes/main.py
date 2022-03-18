# Created by Kelvin_Clark on 3/10/22, 1:10 PM
import os
import uuid
from flask import Blueprint, render_template, request, jsonify, send_file

from .dependencies.session import login_required
from src.core.qr_generator import generate_qr_code_image
from src.utils.hex_to_rgb import hex_to_rgb

main_router = Blueprint("main", import_name=__name__)


@main_router.route("/")
@login_required
def main_index():
    return render_template("main/index.html")


@main_router.route("/decodeQrCode/", methods=["GET", "POST"])
@login_required
def decode_qr():
    return render_template("main/decode.html")


@main_router.route("/generateQrCode/", methods=["POST", "GET"])
@login_required
def generate_qr():
    json = request.json
    if json is None:
        return jsonify({"error": "Expected JSON payload, but received something different"}), 400
    try:
        json = __process_color_params(json)
        image = generate_qr_code_image(**json)
    except TypeError as e:
        print(e)
        return jsonify({"error": "Make sure you're passing all required fields"}), 400
    if not image:
        return jsonify({"error": "Something didn't go well, check your payload or try again later"}), 400
    file_name = f"{uuid.uuid1()}.png"
    image.save(f"tmp{os.path.sep}{file_name}")
    from app import tmp_folder
    return send_file(f"{os.path.join(tmp_folder, file_name)}", mimetype="image/png",
                     attachment_filename="qr_code_image.png", as_attachment=True)


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
