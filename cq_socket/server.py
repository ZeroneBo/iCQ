# server.py
"""
此时服务端为本机5701端口，客户端为CQ
CQ向本机5701发请求，请求内容为收到的事件及其内容
"""
from flask import Flask, request
from cq_handle import cqclassfy


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def process():
    """
    :return: 响应客户端的内容为空字符串
    """
    # 经过测试，gocq请求方式为 POST
    if request.method == 'POST':
        content = request.get_json()
        cqclassfy.handle(content)
    elif request.method == 'GET':
        pass
    else:
        pass
    return ""


def run():
    """
    监听5701端口
    """
    app.run(host='127.0.0.1', port=5701)
