# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DouyuPipeline(object):

    def __init__(self):
        self.fp = open("douyuinfo.html","w",encoding="utf-8")
        self.fp.write("<html><head><meta charset='utf-8'><title>一个html文件</title><style>img{width:50px;}table{width:100%;cellspacing:0;border-collapse: collapse;border-right: 1px solid #ccc;border-bottom: 1px solid #ccc;}tr{padding:15px}td{margin:0px;text-align: center;height: 50px;line-height: 30px;border-left: 1px solid #ccc;border-top: 1px solid #ccc;}th{width:33%}</style></head><table><th>主播名字</th><th>房间id</th><th>头像</th>")

    def process_item(self, item, spider):
        self.fp.write(''.join(["<tr><td>",item['nickname'],"</td>","<td>",item['roomid'],"</td>","<td>",f'<img src="{item["imagelink"]}"/>',"</td></tr>"]))
        return item

    def spider_close(self):
        self.fp.write("</table></html>")
        self.fp.close()
