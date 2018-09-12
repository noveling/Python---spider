# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import base64


class TkcrawlerPipeline(object):
    def __init__(self):
        self.fp = open("tikuinfo.html","w",encoding="utf-8")
        self.fp.write("<html><head><meta charset='utf-8'><title>一个html文件</title><style>img{width:50px;}table{width:100%;cellspacing:0;border-collapse: collapse;border-right: 1px solid #ccc;border-bottom: 1px solid #ccc;}tr{padding:15px}td{margin:0px;text-align: center;height: 50px;line-height: 30px;border-left: 1px solid #ccc;border-top: 1px solid #ccc;}</style></head><table><th>题目标题</th><th>题目限制</th><th>题目描述</th><th>标准输入</th><th>标准输出</th><th>样例</th><th>线索</th><th>输入次数</th><th>正确数</th><th>地址</th><th>资源</th>")

    def process_item(self, item, spider):
        self.fp.write(''.join(["<tr><td>",item["tname"],"</td>","<td>",item['tlimit'],"</td>","<td>",item['tdes'],"<td>",item['tstdin'],"</td>","<td>",item['tstdout'],"</td>","<td>",item['sample'],"</td>","<td>",item['data'],"</td>","<td>",item['tsub'],"</td>","<td>",item['tpass'],"</td>","<td>",item['turl'],"</td>","<td>",item['source'],"</td>","</tr>\n"]))
        return item

    def spider_close(self):
        self.fp.write("</table></html>")
        self.fp.close()

# class TkcrawlerPipeline(object):
#     def __init__(self):
#         self.connect = pymysql.connect(
#             host = "xxx.xxx.xxx",
#             port = 3306,
#             db = "spider",
#             user = "root",
#             passwd = "123456",
#         )
#         self.cursor = self.connect.cursor()
#
#     def process_item(self, item, spider):
#         self.cursor.execute(
#             '''insert into lydsy_tiku_spider(url,title,label,tags,accept,commint,topicDesc,inputFormat,outputFormat,topicExample,dataExample,source) value (%s,%s,%s,'',%s,%s,%s,%s,%s,%s,%s,%s)''',(item['turl'],item['tname'],item['tlimit'],item['tpass'],item['tsub'],base64.b64encode(item['tdes'].encode("utf-8")),base64.b64encode(item['tstdin'].encode("utf-8")),base64.b64encode(item['tstdout'].encode("utf-8")),base64.b64encode(item['sample'].encode("utf-8")),base64.b64encode(item['data'].encode("utf-8")),item['source']),
#         )
#         self.connect.commit()
#
#         return item
#
#     def spider_close(self):
#         self.cursor.close()
#         self.connect.close()
