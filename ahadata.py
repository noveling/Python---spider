import requests
from multiprocessing.dummy import Pool as ThreadPool
import json
import pymysql
import codecs

import sys


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = codecs.open(fileN, "a", "utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger("D:\\datalog8.txt")


access_token = "14_oDFsoODedABmCL-jVNIgWm-9VcUP4pmRaKuxBFZSmyFQBtDAMiYq2UUdYylZvO1T_PShLOlhA5v9pfjAKsFodhdWzIq-WAJI0x8PZLl3g3zR92ZrbhzwtA89kZBC0-12J3TVIbVQ-m6THQP-TDLfAHANXF"

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}

name_link = []
url_data = []


with open("C:\\Users\\Administrator\\Desktop\\新建文本文档.txt", "r") as f:
    for i in f:
        name_link.append(i.strip())

print(len(name_link))

for i in name_link:
    url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=" + \
        access_token + "&openid=" + str(i) + "&lang=zh_CN"
    url_data.append(url)
print(len(url_data))


def parse_url(url):
    try:
        connect = pymysql.connect(
            host="192.168.31.105",
            port=3306,
            db="spider",
            user="root",
            passwd="123456",
        )
        cursor = connect.cursor()
        res = requests.get(url, headers=head)
        res.encoding = "utf-8"
        res_dict = json.loads(res.text)
        print(url)
        print(res_dict)
        if "nickname" in res_dict:
            cursor.execute(
                '''insert into twx_users(subscribe,openid,nickname,sex,language,city,province,country,headimgurl,subscribe_time,subscribe_scene) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update subscribe=%s,openid=%s,nickname=%s,sex=%s,language=%s,city=%s,province=%s,country=%s,headimgurl=%s,subscribe_time=%s,subscribe_scene=%s''',
                (res_dict['subscribe'],
                 res_dict['openid'],
                    res_dict['nickname'],
                    res_dict['sex'],
                    res_dict['language'],
                    res_dict['city'],
                    res_dict['province'],
                    res_dict['country'],
                    res_dict['headimgurl'],
                    res_dict['subscribe_time'],
                    res_dict['subscribe_scene'],
                    res_dict['subscribe'],
                    res_dict['openid'],
                    res_dict['nickname'],
                    res_dict['sex'],
                    res_dict['language'],
                    res_dict['city'],
                    res_dict['province'],
                    res_dict['country'],
                    res_dict['headimgurl'],
                    res_dict['subscribe_time'],
                    res_dict['subscribe_scene']))
            connect.commit()
        else:
            print("就是", res_dict)
            cursor.execute(
                '''insert into twx_users(subscribe,openid) value (%s,%s) on duplicate key update subscribe=%s,openid=%s''',
                (res_dict['subscribe'], res_dict['openid'], res_dict['subscribe'], res_dict['openid']))
            connect.commit()
    except Exception as e:
        print("有错误Error:", e)

    finally:
        cursor.close()
        connect.close()


pool = ThreadPool(10)
pool.map(parse_url, url_data)


pool.close()
pool.join()
