# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

# class SimplespiderPipeline(object):

    # def __init__(self):
    #     self.tf = open("result.json",'w',encoding="utf-8")
    #
    # def process_item(self, item, spider):
    #     print(item["name"])
    #     print(item["link"])
    #     json.dump(dict(item),self.tf,ensure_ascii=False)
    #     return item
    #
    # def spider_closed(self, spider):
    #     self.tf.close()

class SimplespiderPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self):
        # self.file = open('data.json', 'wb')
        self.file = codecs.open(
            'scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
