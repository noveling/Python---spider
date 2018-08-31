# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    birth = scrapy.Field()
    sex = scrapy.Field()
    fate = scrapy.Field()
    score1 = scrapy.Field()
    score2 = scrapy.Field()