# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from getname.items import GetnameItem
import re


class CrawlnameSpider(CrawlSpider):
    name = 'crawlname'
    allowed_domains = ['xh.5156edu.com']
    start_urls = ['http://xh.5156edu.com/xm/nu.html']

    rules = (
        Rule(
            LinkExtractor(
                allow=r'http://xh.5156edu.com/xm/.+'),
            callback='parse_item',
            follow=True),
    )

    def parse_item(self, response):
        i = GetnameItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        namelist = response.xpath('//td[@width="16%"]/text()').extract()
        for name in namelist:
            finalname = re.sub(r"['(',')',' ','\n']", '', name, flags=re.S)
            if finalname:
                i['ming'] = finalname
                yield i
