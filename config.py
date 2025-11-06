import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev_secret_key"
    # MySQL 配置，格式: mysql+pymysql://用户名:密码@主机/数据库名
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "mysql+pymysql://root:@127.0.0.1/kyo_admin"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
