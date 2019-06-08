from flask import Flask, session
# 导入flask_session扩展包，用来指定session信息储存的位置
from flask_session import Session
# 导入配置对象
from config import Config
#使用管理器
from flask_script import Manager
# 导入flask_sqlalchemy扩展，实现数据库的链接
from flask_sqlalchemy import SQLAlchemy

from HongMo import create_app

app = create_app('development')

manage = Manager(app)

@app.route('/')
def index():
    session['hongmo'] = '2018'
    return "HongMo"

if __name__ == '__main__':
    manage.run()