# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from scrapy.exceptions import DropItem

class GetnamePipeline(object):
    def __init__(self):
        self.csvfile = open("storename.csv",'w')
        self.name_set = set()

    def process_item(self, item, spider):
        namejudge = item["ming"]
        if namejudge in self.name_set:
            raise DropItem("重复内容"+namejudge)
        self.name_set.add(namejudge)
        mywriter = csv.writer(self.csvfile)
        name = item["ming"]
        print(name)
        mywriter.writerow([name,])
        return item

    def spider_close(self):
        self.csvfile.close()
