from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 数据库实例


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from .routes.main import main_bp
    from .routes.user_route import user_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    db.init_app(app)  # 初始化数据库

    return app
