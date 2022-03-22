# Created by Kelvin_Clark on 3/10/22, 1:10 PM
import os
import imghdr
import uuid
from flask import Blueprint, render_template, request, jsonify, send_file, flash, redirect, url_for

from .dependencies.general import __process_color_params
from .dependencies.session import login_required
from src.core.qr_generator import generate_qr_code_image
from src.core.qr_decoder import decode_qr_code
from src.utils.enum.flash_message_category import FlashMessageCategory

main_router = Blueprint("main", import_name=__name__)


@main_router.route("/")
@login_required
def main_index():
    return render_template("main/index.html")


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


@main_router.route('/decodeQrCode/', methods=["POST"])
@login_required
def decode_qr():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part present", category=FlashMessageCategory.ERROR.value)
            return redirect(location=url_for(endpoint="main.main_index"))
        file = request.files["file"]
        if file.filename == "":
            flash("No file selected", category=FlashMessageCategory.ERROR.value)
            return redirect(location=url_for(endpoint="main.main_index"))
        is_image_file = imghdr.what(file=file.stream)
        if is_image_file is None:
            flash("File not a valid image", category=FlashMessageCategory.WARNING.value)
            return redirect(location=url_for(endpoint="main.main_index"))
        data = decode_qr_code(file)
        response = []
        for d in data:
            response.append(d.data.decode())
        return jsonify({"data": response})



