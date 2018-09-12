# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TkcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    turl = scrapy.Field()
    tname = scrapy.Field()
    tlimit = scrapy.Field()
    # tlabel = scrapy.Field()
    tpass = scrapy.Field()
    tsub = scrapy.Field()
    tdes = scrapy.Field()
    tstdin = scrapy.Field()
    tstdout = scrapy.Field()
    sample = scrapy.Field()
    source = scrapy.Field()
    data = scrapy.Field()
