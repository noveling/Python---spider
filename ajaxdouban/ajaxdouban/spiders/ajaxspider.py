# -*- coding: utf-8 -*-
import scrapy
from ajaxdouban.items import AjaxdoubanItem
import json
from scrapy.conf import settings


class AjaxspiderSpider(scrapy.Spider):
    # 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='
    # 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=100'
    name = 'ajaxspider'
    allowed_domains = ['douban.com']
    page_offset = 0
    flag = 1
    cook = settings['COOKIE']
    baseurl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='
    start_urls = [''.join([baseurl, str(page_offset)])]

    def parse(self, response):
        item = AjaxdoubanItem()
        data = json.loads(response.text)["subjects"]
        # data = json.loads(response.text)["data"]
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
            yield scrapy.Request(''.join([self.baseurl, str(self.page_offset)]), cookies=self.cook, callback=self.parse)
            # print(response.request.headers)
