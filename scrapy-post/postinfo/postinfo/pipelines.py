# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class PostinfoPipeline(object):
    def __init__(self):
        self.csvfile = open("storescore.csv","w", newline='')
        mywriter = csv.writer(self.csvfile)
        mywriter.writerow(["名字","性别","生日","命宫","姓名评分","生辰评分"])

    def process_item(self, item, spider):
        allinfo = [item["name"][0],item["sex"][0],item["birth"][0],item["fate"][0],item["score1"][0],item["score2"][0]]
        mywriter = csv.writer(self.csvfile)
        mywriter.writerow(allinfo)
        return item

    def spider_close(self):
        self.csvfile.close()


