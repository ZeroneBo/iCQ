# cqclassfy.py
"""
对从5701收到的事件进行分类处理
"""
from cq_handle import cqmessage, cqnotice, cqrequest


def handle(content):
    """
    根据事件类型分类，分别处理
    :param content: 收到的json事件内容
    :return:
    """
    post_type = content['post_type']
    if post_type == 'message':  # 消息事件
        cqmessage.message_handle(content)
    elif post_type == 'notice':  # 通知事件
        cqnotice.notice_handle(content)
    elif post_type == 'request':  # 请求事件
        cqrequest.request_handle(content)
