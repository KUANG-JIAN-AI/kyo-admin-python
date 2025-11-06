# app/routes/user_route.py
import random
import time
from app import db
from faker import Faker
from flask import Blueprint, jsonify, render_template, request

from app.models.user_model import User
from app.services.user_service import UserService

user_bp = Blueprint("user", __name__, url_prefix="/user")
service = UserService()


@user_bp.route("/list.html")
def user_tpl():
    return render_template("/user/list.html")


@user_bp.route("/", methods=["GET"])
def list_users():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    # 收集参数
    params = {
        "username": request.args.get("username"),
        "email": request.args.get("email"),
        "phone": request.args.get("phone"),
        "status": request.args.get("status"),
    }

    # 去除空值字段
    filters = {k: v for k, v in params.items() if v not in (None, "", "null")}
    print("filters=", filters, type(filters))

    result = service.paginate(page=page, per_page=per_page, filters=filters)
    return jsonify({"code": 200, "msg": "success", "data": result})


@user_bp.route("/add_test", methods=["GET"])
def add_test_users():
    """自动生成测试用户数据
    示例: GET /user/add_test?count=10
    """
    # 获取参数 count（默认为 5）
    count = int(request.args.get("count", 5))

    fake = Faker("ja_JP")  # 生成日本风格的假数据
    created_users = []

    for _ in range(count):
        username = f"{fake.user_name()}_{random.randint(1000, 9999)}"
        email = fake.email()
        phone = fake.phone_number()
        password = "pbkdf2:sha256:260000$xyz$test123"

        user = User(
            username=username,
            password=password,
            email=email,
            phone=phone,
            created_at=int(time.time()),
            updated_at=int(time.time()),
        )
        db.session.add(user)
        created_users.append(user)

    db.session.commit()

    return jsonify(
        {
            "message": f"成功生成 {len(created_users)} 条测试数据",
            "data": [u.to_dict() for u in created_users],
        }
    )
