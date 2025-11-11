import os
import uuid

from flask import current_app, request


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


class UploadService:
    def save_file(self, file):
        """保存上传文件并返回新文件名与访问URL"""
        if not file or file.filename == "":
            return None, "未选择文件"

        if not allowed_file(file.filename):
            return None, "文件类型不允许"

        ext = file.filename.rsplit(".", 1)[1].lower()
        new_filename = f"{uuid.uuid4().hex}.{ext}"
        upload_folder = os.path.join(current_app.root_path, "static", "uploads")
        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(upload_folder, new_filename)
        file.save(file_path)

        # ✅ 拼接完整 URL（自动带端口）
        file_url = f"{request.host_url}static/uploads/{new_filename}"

        # 去掉可能的重复斜杠
        file_url = file_url.replace("///", "//")

        return file_url, None
