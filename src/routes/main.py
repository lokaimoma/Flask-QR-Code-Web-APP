# Created by Kelvin_Clark on 3/10/22, 1:10 PM
import os
import io
from flask import Blueprint, render_template, request, jsonify, send_file

from .dependencies.session import login_required
from src.core.qr_generator import generate_qr_code_image

main_router = Blueprint("main", import_name=__name__)


@main_router.route("/")
@login_required
def main_index():
    return render_template("main/index.html")


@main_router.route("/generateQrCode/", methods=["POST"])
@login_required
def generate_qr():
    json = request.json
    if json is None:
        return jsonify({"error": "Expected JSON payload, but received something different"}), 404
    image = generate_qr_code_image(**json)
    if not image:
        return jsonify({"error": "Make sure you're passing all required fields"}), 404
    file = io.BytesIO()
    image.save(file)
    return send_file(file, mimetype="image/png", download_name="qr_code_image.png")
