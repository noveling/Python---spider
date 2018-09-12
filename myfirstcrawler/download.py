# -*- coding: cp936 -*-
#download
import urllib2
import lxml.html
from bs4 import BeautifulSoup


def download(url = 'https://www.baidu.com/', num_retires = 2):
    '''下载网页的html'''
    print 'downloadurl' ,url
    header =\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'}
    request = urllib2.Request(url,headers = header)
    try:
       html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'downloaderror',e.reason
        html = None
        if num_retires > 0:
            if hasattr(e, 'code') and  500 <= e.code < 600:
                return download(url, num_retires-1)
    return html




if __name__ == '__main__':
    out = raw_input('请输入一个内容')
    html = download()
    soup = BeautifulSoup(html,'html.parser')
    print soup.title
    print 'starting to find_________________________________________!'
    tree = lxml.html.fromstring(html)
    fixed_html = lxml.html.tostring(tree, pretty_print = True)
    print fixed_html
    
