from flask import Flask, request
import sqlite3
from callwx import callwx
app = Flask(__name__)


# API 端点，接收数据并插入到数据库
@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json  # 从 POST 请求中获取 JSON 数据
    name = data.get('name')
    wechat = data.get('wechat')
    conn = sqlite3.connect('/app/data/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO userWait (name, wechat) VALUES (?, ?)', (name, wechat))
    conn.commit()
    conn.close()
    callwx(name, wechat)
    return 'ok' 
if __name__ == '__main__':
    app.run(host="0.0.0.0",  debug=True)  # 启动 Flask 应用
