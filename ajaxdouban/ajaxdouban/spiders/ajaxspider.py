# -*- coding: utf-8 -*-
import scrapy
from ajaxdouban.items import AjaxdoubanItem
import json

class AjaxspiderSpider(scrapy.Spider):
    name = 'ajaxspider'
    allowed_domains = ['douban.com']
    page_offset = 0
    flag = 1
    baseurl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='
    start_urls = [''.join([baseurl,str(page_offset)])]

    def parse(self, response):
        item = AjaxdoubanItem()
        data = json.loads(response.text)["subjects"]
        # print(data)
        if data:
            for each in data:
                item["moviename"] = each["title"]
                item["movieimg"] = each["cover"]
                item["score"] = each["rate"]
                item["movieurl"] = each["url"]
                yield item
        else:
            self.flag = 0
        self.page_offset += 20
        if self.flag:
            yield scrapy.Request(''.join([self.baseurl,str(self.page_offset)]),callback=self.parse)
