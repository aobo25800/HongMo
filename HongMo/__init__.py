from flask import Flask
# 导入Config类， 导入config_dict字典
from config import Config, config_dict
# 导入flask_session扩展包，用来指定session信息储存的位置
from flask_session import Session
# 导入flask_sqlalchemy扩展， 实现数据库的链接
from flask_sqlalchemy import SQLAlchemy


# 定义工厂函数，让函数根据参数的不容，生产不同环境下的app，即开发模式下的app或生产环境下的app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    Session(app)
    db = SQLAlchemy(app)

    return app