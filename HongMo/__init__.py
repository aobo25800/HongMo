from flask import Flask
# 导入Config类， 导入config_dict字典
from config import Config, config_dict
# 导入flask_session扩展包，用来指定session信息储存的位置
from flask_session import Session
# 导入flask_sqlalchemy扩展， 实现数据库的链接
from flask_sqlalchemy import SQLAlchemy
# logging python标准模块
import logging
from logging.handlers import RotatingFileHandler

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG) # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)

# 定义工厂函数，让函数根据参数的不容，生产不同环境下的app，即开发模式下的app或生产环境下的app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    Session(app)
    db = SQLAlchemy(app)

    return app