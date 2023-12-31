from flask import Flask, request,render_template
import sqlite3
from callwx import callwx
app = Flask(__name__)

##########################
#CREATE TABLE IF NOT EXISTS userWait (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    email TEXT NOT NULL,
#    wechat TEXT NOT NULL,
#    want TEXT NOT NULL,
#    done INTEGER DEFAULT 0
#);
##########################
# API 端点，接收数据并插入到数据库
@app.route('/')
def root():
    return render_template('index.html')
@app.route('/add', methods=['POST'])
def insert_data():
    data = request.form  # 从 POST 请求中获取 JSON 数据
    email = data.get('email')
    wechat = data.get('wechat')
    want = data.get('want')
    conn = sqlite3.connect('/app/data/database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO userWait (email, wechat,want) VALUES (?, ?,?)', (email, wechat,want))
    conn.commit()
    conn.close()
    callwx(email, wechat,want)
    return render_template('done.html',version="基础版")

@app.route('/base')
def base():
    #version
    return render_template('add.html',version="基础版")

@app.route('/bind')
def bind():
    return render_template('add.html',version="绑定版")

@app.route('/pro')
def pro():
    return render_template('add.html',version="高级版")

if __name__ == '__main__':
    app.run(host="0.0.0.0",  debug=True) 
