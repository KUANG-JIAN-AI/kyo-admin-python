# app/models/user_models.py
import time
from app import db
from app.utils import format_time


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    avatar = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(db.Integer, default=lambda: int(time.time()))
    updated_at = db.Column(
        db.Integer, default=lambda: int(time.time()), onupdate=lambda: int(time.time())
    )
    deleted_at = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        """模型转字典"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "avatar": self.avatar,
            "status": self.status,
            "status_text": "正常" if self.status == 1 else "异常",
            "created_at": format_time(self.created_at),
            "updated_at": format_time(self.updated_at),
            "deleted_at": format_time(self.deleted_at),
        }

    def __repr__(self):
        return f"<User {self.username}>"
