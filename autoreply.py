#coding=utf8
import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

#添加
'''
import re
import time

import itchat
from itchat.content import *

@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    print(msg['Text'])

@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])

@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    if msg['Type'] == 'Text':
        reply_content = msg['Text']
    elif msg['Type'] == 'Picture':
        reply_content = r"图片: " + msg['FileName']
    elif msg['Type'] == 'Card':
        reply_content = r" " + msg['RecommendInfo']['NickName'] + r" 的名片"
    elif msg['Type'] == 'Map':
        x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1,
                                                                                                                    2,
                                                                                                                    3)
        if location is None:
            reply_content = r"位置: 纬度->" + x.__str__() + " 经度->" + y.__str__()
        else:
            reply_content = r"位置: " + location
    elif msg['Type'] == 'Note':
        reply_content = r"通知"
    elif msg['Type'] == 'Sharing':
        reply_content = r"分享"
    elif msg['Type'] == 'Recording':
        reply_content = r"语音"
    elif msg['Type'] == 'Attachment':
        reply_content = r"文件: " + msg['FileName']
    elif msg['Type'] == 'Video':
        reply_content = r"视频: " + msg['FileName']
    else:
        reply_content = r"消息"

    friend = itchat.search_friends(userName=msg['FromUserName'])
    itchat.send(r"Friend:%s -- %s    "
                r"Time:%s    "
                r" Message:%s" % (friend['NickName'], friend['RemarkName'], time.ctime(), reply_content),
                toUserName='filehelper')

    itchat.send(r"我已经收到你在【%s】发送的消息【%s】稍后回复。--微信助手(Python版)" % (time.ctime(), reply_content),
                toUserName=msg['FromUserName'])


itchat.auto_login()
itchat.run()
'''
#添加

def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    # reply = get_response(msg['Text'])
    reply = "message:"+msg['Text']+"我收到了你的信息，但是嫌弃的拒绝接收，( ∪.∪ )... zzz ZZZ 呼噜呼噜……I received your message, but refused to receive it."
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.run()
