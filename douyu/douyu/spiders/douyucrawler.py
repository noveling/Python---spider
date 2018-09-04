# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DouyucrawlerSpider(scrapy.Spider):
    flag = 1
    name = 'douyucrawler'
    allowed_domains = ['capi.douyucdn.cn']
    # start_urls = ['http://capi.douyucdn.cn/']

    baseurl = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    actualurl = ''.join([baseurl,str(offset)])

    start_urls= [actualurl]

    def parse(self, response):
        data = json.loads(response.text)['data']
        if data:
            for each in data:
                item = DouyuItem()
                item['nickname'] = each['nickname']
                item['imagelink'] = each['vertical_src']
                item['roomid'] = each['room_id']
                yield item
        else:
            self.flag = 0
        if self.flag:
            self.offset += 20
            yield scrapy.Request(''.join([self.baseurl,str(self.offset)]),callback=self.parse)
