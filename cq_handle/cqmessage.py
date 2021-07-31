# cqmessage.py
"""
对消息事件处理
"""
import json
from cq_socket import client
from fun_api import ibot, netease


def message_handle(content):
    """
    消息分类，分别处理
    """
    message_type = content['message_type']
    message_id = None
    if message_type == 'private':
        message_id = send_private_msg(content)
    elif message_type == 'group':
        message_id = send_group_msg(content)
    # message_id 如何保存？可用于转发、撤回……


def send_private_msg(content):
    """
    # 私聊消息处理，生成回复消息
    """
    recv = content['message']
    user_id = content['user_id']
    send = fun_msg(recv, user_id)
    resp = {
        "user_id": user_id,
        "message": send,
        "auto_escape": False
    }
    resp = client.request_post('send_private_msg', resp)
    resp = json.loads(resp)
    message_id = resp['data']['message_id']
    return message_id


# 群聊消息处理
def send_group_msg(content):
    """
    # 群消息处理，生成回复消息
    """
    if content['anonymous']:
        pass
    else:
        recv = content['message']
        group_id = content['group_id']
        send = fun_msg(recv, group_id)
        resp = {
            "group_id": group_id,
            "message": send,
            "auto_escape": False
        }
        resp = client.request_post('send_group_msg', resp)
        resp = json.loads(resp)
        message_id = resp['data']['message_id']
        return message_id


def fun_msg(recv, user_id):
    if recv == '#':
        send = '''\
功能菜单如下:

#: 查看功能菜单
#bot: 机器人聊天
#chp: 彩虹屁
#dz:  讲段子
#pyq: 朋友圈文案
#pz:  喷子
#wyy: 网抑云风格评论

(彩蛋: 隐藏功能,多多探索 ^_^)'''
    elif recv == '#chp':
        send = ibot.chp()
    elif recv == '#pyq':
        send = ibot.pyq()
    elif recv == '#pz':
        send = ibot.penzi()
    elif recv == '#duanzi':
        send = ibot.duanzi()
    elif recv == '#netease':
        send = netease.get_comment()
    elif recv == '#bot':
        send = ibot.sizhi(recv, user_id)
    else:
        send = ibot.sizhi(recv)
    # send = send.replace(' ', '%20')
    # send = send.replace('\n', '%0d')
    return send
