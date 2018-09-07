# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class AjaxdoubanPipeline(object):
    def __init__(self):
        self.fp = codecs.open('movielist.html','w',encoding='utf-8')
        self.fp.write("<html><head><meta charset='utf-8'/><title>豆瓣电影清单</title><style>table{font-size:20px}</style></head><table><th>电影名</th><th>评分</th><th>电影链接</th><th>图片</th>")

    def process_item(self, item, spider):
        self.fp.write("<tr><td>"+item['moviename']+"</td><td>"+item['score']+"</td><td>"+item['movieurl']+"</td><td><img src='"+item['movieimg']+"'></td></tr>")
        return item

    def spider_close(self):
        self.fp.write("</table></html>")
        self.fp.close()
