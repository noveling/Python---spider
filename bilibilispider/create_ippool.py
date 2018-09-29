import requests
import re

def get_html(num = 10):
    res = requests.get("http://www.89ip.cn/tqdl.html?api=1&num="+str(num)+"&port=&address=&isp=")
    html = res.text
    return get_url(html)

def get_url(html):
    comp = re.compile(r"\d+?\.\d+?\.\d+?\.\d+?:\d+")
    res = comp.findall(html)
    return res


if __name__ == "__main__":
    print(get_html(30))