import hashlib
import json
import random
import re
import urllib
import requests


def sizhi(question, user_id='0'):
    question = re.sub(r'#\w*\s*', '', question)
    if not question:
        question = '你是谁'
    data = {
        "userid": user_id,
        "spoken": question
    }
    r = requests.post('https://api.ownthink.com/bot', data=data)
    answer = r.json()['data']['info']['text']
    return answer


def xiaoi(question, user_id='0'):
    """智障机器人"""
    question = re.sub(r'#\w*\s*', '', question)

    # 两个函数：
    def getNonce():
        strs = ''
        for i in range(18):
            strs += (str(random.randint(0, 15)))
        return strs

    t = ""
    with open('.config', 'r', encoding='utf8') as fp:
        f_data = json.load(fp)
        appKey = f_data['appKey']
        appSecret = f_data['appSecret']
    HA1 = hashlib.sha1(
        ':'.join([appKey, "xiaoi.com", appSecret]).encode("utf8")).hexdigest()
    HA2 = hashlib.sha1(u"GET:/ask.do".encode("utf8")).hexdigest()
    nonce = getNonce()  # ':'.join([HA1, nonce, HA2]).encode("utf8")
    sig = hashlib.sha1(
        ':'.join([HA1, nonce, HA2]).encode("utf8")).hexdigest()

    headers = {
        "X-Auth": "app_key=\"{0}\",nonce=\"{1}\",signature=\"{2}\"".format(
            appKey, nonce, sig)
    }
    post_data = {
        "question": question,
        "userId": user_id,
        "type": t,
        "platform": "web"
    }
    post_data = urllib.parse.urlencode(post_data)
    url = "http://robot.open.xiaoi.com/ask.do?" + post_data
    request = urllib.request.Request(url, None, headers)
    request.add_header('Content-Type', 'text/html; charset=UTF-8')
    response = urllib.request.urlopen(request)
    return str(response.read(), 'utf8')


def duanzi():
    r = requests.get('http://www.yduanzi.com/?utm_source=shadiao.app')
    text = r.text
    text = re.search(r"duanzi-text'>(.*)<", text).group(1)
    text = re.sub(r'<.*?>', '', text)
    return text


def chp():
    r = requests.get('https://api.shadiao.app/chp')
    text = json.loads(r.text)['data']['text']
    return text


def penzi(level='min'):
    if level not in ['max', 'min']:
        level = random.choice(['max', 'min'])
    r = requests.get('https://api.shadiao.app/nmsl?level=' + level)
    text = json.loads(r.text)['data']['text']
    return text


def pyq():
    r = requests.get('https://api.shadiao.app/pyq')
    text = json.loads(r.text)['data']['text']
    return text


def medals():
    url = 'http://api.cntv.cn/olympic/getOlyMedals'
    params = {
        "serviceId": "pcocean",
        "itemcode": "GEN-------------------------------",
    }
    r = requests.get(url=url, params=params)
    data = r.json()
    data = data['data']['medalsList'][:10]
    medal = "%s %s %s %s %s" % ('国家', '金', '银', '铜', '总')
    medal += '\n============='
    for country in data:
        line = "\n%s %s %s %s %s" % (
            country['countryname'], country['gold'], country['silver'], country['bronze'], country['count'])

        medal += line
    return medal


def wyy():
    comment = ""
    with open('wangyiyun.txt', 'r', encoding='utf8') as f:
        rand = random.randint(0, 200)
        index = 0
        for line in f.readlines():
            if index < rand:
                if line == "\n":
                    index += 1
                else:
                    continue
            elif index == rand and line != "\n":
                comment += line
            else:
                break
    comment = comment.strip()
    return comment
