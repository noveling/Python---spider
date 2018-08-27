import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.http import Request
from myspider.items import MyspiderItem


class Myspider(scrapy.Spider):

    name = "dingdian"
    allowed_domains = ['23wx.cc']
  
    bash_url = "http://www.23wx.cc/class/"
    bashurl = ".html"
    num = 1

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)

    def parse(self, response):
        namelist = []
        urllist = []
        regex = re.compile(r'^https:.*', re.S)
        name = BeautifulSoup(response.text, 'lxml').find_all(
            'span', attrs={"class": "s2"})
        for i in name:
            namelist.append(i.find('a').string)
            if regex.findall(i.find('a')['href']):
                urllist.append(i.find('a')['href'])
            else:
                urllist.append(
                    ''.join(['https://www.23wx.cc',i.find('a')['href']]))
        if len(namelist) == len(urllist):
            res = zip(namelist, urllist)
        for i in res:
            item = MyspiderItem()
            item["name"] = i[0]
            item["content"] = i[1]
            yield item
            print(i)
