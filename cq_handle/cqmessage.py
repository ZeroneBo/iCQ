# cqmessage.py
"""
对消息事件处理
"""
import json
import re
from cq_socket import client
from fun_api import ibot


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
============
#:\t查看功能菜单
#功能 #:\t查看功能参数
#bot*:\t机器人聊天
#chp:\t彩虹屁
#dz:\t讲段子
#medal:\t东京奥运奖牌榜
#pyq:\t朋友圈文案
#pz*:\t喷子
#wyy:\t网抑云
============
*表示该功能可加参数,不需输入*'''
    elif recv == '#chp':
        send = ibot.chp()
    elif recv == '#pyq':
        send = ibot.pyq()
    elif recv == '#dz':
        send = ibot.duanzi()
    elif recv == '#medal':
        send = ibot.medals()
    elif recv == '#wyy':
        send = ibot.wyy()
    elif re.match(r'#pz', recv):
        level = None
        if re.search(r'\s+#$', recv):
            send = 'max -火力较大\nmin -火力一般\n如: #pz max'
        else:
            if re.search(r'\s+max\s+|\s+max$', recv):
                level = 'max'
            elif re.search(r'\s+min\s+|\s+min$', recv):
                level = 'min'
            send = ibot.penzi(level)
    elif re.match(r'#bot', recv):
        if re.search(r'\s+#$', recv):
            send = 'cm -聪明点的聊天机器人\nsz -傻一点的聊天机器人\n如: #bot cm 问题'
        else:
            if re.search(r'\s+cm\s+|\s+cm$', recv):
                send = ibot.sizhi(recv, user_id)
            elif re.search(r'\s+sz\s+|\s+sz$', recv):
                send = ibot.xiaoi(recv, user_id)
            else:
                send = ibot.sizhi(recv, user_id)
    else:
        send = ibot.sizhi(recv)
    # send = send.replace(' ', '%20')
    # send = send.replace('\n', '%0d')
    return send
