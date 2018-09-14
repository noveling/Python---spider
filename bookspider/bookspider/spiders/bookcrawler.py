# -*- coding: utf-8 -*-
#__author__ = "noveling"
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bookspider.items import BookspiderItem
import re


class BookcrawlerSpider(CrawlSpider):
    name = "bookcrawler"
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/']

    rules = (
        Rule(LinkExtractor(allow=r'^https://book.douban.com/tag/.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = BookspiderItem()
        info = []
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        nameinfo = response.xpath("//ul/li/div[@class='info']/h2[@class]/a/text()").extract()
        for name in nameinfo:
            final = re.sub(r"[' ','\n']","",name,flags=re.S)
            if final:
                info.append(final)
        i["bookurl"] = response.xpath("//ul/li/div[@class='info']/h2[@class]/a/@href").extract()
        i["bookname"] = info

        yield i
