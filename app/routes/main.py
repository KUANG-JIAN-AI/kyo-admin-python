from flask import Blueprint, jsonify, render_template, request

from app.services.upload_service import UploadService

# app/routes/main.py
main_bp = Blueprint("main", __name__, url_prefix="/")

service = UploadService()


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    url, error = service.save_file(file)

    if error:
        return jsonify({"code": 400, "msg": error})

    return jsonify({"code": 200, "msg": "上传成功", "url": url})
