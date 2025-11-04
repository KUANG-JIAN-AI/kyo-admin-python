from flask import Blueprint, render_template

# app/routes/main.py
main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/")
def index():
    return render_template("index.html")
