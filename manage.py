from flask import Flask, session
# 导入flask_session扩展包，用来指定session信息储存的位置
from flask_session import Session
# 导入配置对象
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

Session(app)
@app.route('/')
def index():
    session['hongmo'] = '2018'
    return "HongMo"

if __name__ == '__main__':
    app.run(debug=True)