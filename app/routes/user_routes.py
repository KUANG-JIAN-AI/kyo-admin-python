# app/routes/user_routes.py
from flask import Blueprint, render_template

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/list.html")
def user_list():
    return render_template("/user/list.html")
