# client.py
"""
客户端，向5700端口发请求
"""
# 在5700端口的角度上，我们是发送消息的客户端
import requests


def request_post(api, resp):
    """POST 方式发请求
    :param api: 调用的CQ的API
    :param resp: post方式的data部分
    :return:
    """
    url = 'http://127.0.0.1:5700/' + api
    r = requests.post(url=url, data=resp)
    return r.text

    # # socket方式发送 POST 或 GET 请求
    # ip = '127.0.0.1'
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect((ip, 5700))
    # msg_type = resp['message_type']  # 回复类型（群聊/私聊）
    # number = resp['user_id']  # 回复账号（群号/好友号）
    # msg = resp['message']  # 要回复的消息
    # msg = sizhi(msg)
    # payload = ""
    # if msg_type == 'group':
    #     payload = "GET /send_group_msg?group_id=" + str(
    #         number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    # elif msg_type == 'private':
    #     payload = "GET /send_private_msg?user_id=" + str(
    #         number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    # client.send(payload.encode("utf-8"))
    # client.close()
