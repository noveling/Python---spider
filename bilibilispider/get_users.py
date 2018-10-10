import requests
import time
from multiprocessing.dummy import Pool as ThreadPool
import json
import random
from create_ippool import get_html
import os
from urllib.request import urlretrieve

ip_pool = [{"http":"http://"+i} for i in get_html(20)]
print(ip_pool)

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/45388',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}



def current_milli_time():
    return int(round(time.time() * 1000))


urls = []

# Please change the range data by yourself.
for m in range(1000, 8000):

    for i in range(m * 100, (m + 1) * 100):
        url = 'https://space.bilibili.com/' + str(i)
        urls.append(url)


def getsource(url):
    rel_info={}
    proxy = random.choice(ip_pool)
    print("代理:",proxy)
    payload = {
        '_': current_milli_time(),
        'mid': url.replace('https://space.bilibili.com/', '')
    }
    try:
        jscontent = requests \
            .session() \
            .post('http://space.bilibili.com/ajax/member/GetInfo',
                  headers=head,
                  data=payload,proxies=proxy).text
        rel_info = json.loads(jscontent, encoding="utf-8")
        print(rel_info)
    except:
        try:
            print("更换代理ip")
            proxy = random.choice(ip_pool)
            print("代理:",proxy)
            jscontent = requests \
                .session() \
                .post('http://space.bilibili.com/ajax/member/GetInfo',
                      headers=head,
                      data=payload,proxies=proxy).text
            rel_info = json.loads(jscontent, encoding="utf-8")
            print(rel_info)
        except:
            print("不用代理ip")
            proxy = random.choice(ip_pool)
            print("代理:" ,proxy)
            jscontent = requests \
                .session() \
                .post('http://space.bilibili.com/ajax/member/GetInfo',
                      headers=head,
                      data=payload).text
            rel_info = json.loads(jscontent, encoding="utf-8")
            print(rel_info)
    finally:
        if rel_info["data"] != '服务器遇到了一些问题' and rel_info["data"]["face"]:
            print("downloading......" + rel_info["data"]["face"])
            if not os.path.exists("./image"):
                os.mkdir("./image")

            if not os.path.exists('./image/'+ rel_info["data"]["face"].split('/')[-1]):
                print("正在下载...")
                urlretrieve(rel_info["data"]["face"],'./image/'+ rel_info["data"]["face"].split('/')[-1])
            with open("./bilibili.txt","a") as fp:
                    json.dump(rel_info,fp,ensure_ascii=False)
                    fp.write("\n")



if __name__ == "__main__":
    if os.path.exists("./bilibili.txt"):
        os.remove("./bilibili.txt")
    pool = ThreadPool(5)
    try:
        results = pool.map(getsource, urls)
    except Exception as e:
        print(e)

    pool.close()
    pool.join()
