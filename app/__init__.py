from flask import Flask
from flask_sqlalchemy import SQLAlchemy

_date_ = "2019/1/18 14:59"
_author_ = "xing"


def creat_app():
    """"""
    # __name__ 标识唯一的核心对象
    app = Flask(__name__)
    app.config.from_object("app.secure")
    app.config.from_object("app.settings")

    return app

