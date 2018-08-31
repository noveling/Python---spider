# -*- coding: utf-8 -*-
import scrapy
import csv
from postinfo.items import PostinfoItem



class TestinfoSpider(scrapy.Spider):
    name = 'testinfo'
    allowed_domains = ['threetong.com']
    # start_urls = ['http://threetong.com/']

    def start_requests(self):
        with open(getattr(self, 'file', 'storename.csv')) as f:
            reader = csv.reader(f)
            for line in reader:
                if line:
                    ming = line[0]
                    FormRequest = scrapy.http.FormRequest(
                        url='https://www.threetong.com/ceming/baziceming/xingmingceshi.php',
                        formdata={'isbz': '1',
                                  'txtName': u'刘',
                                  'name': ming,
                                  'rdoSex': '0',
                                  'data_type': '0',
                                  'cboYear': '2018',
                                  'cboMonth': '8',
                                  'cboDay': '31',
                                  'cboHour': u'20-戌时',
                                  'cboMinute': u'39分',
                                  },
                        callback=self.parse  # 这是指定回调函数，就是发送request之后返回的结果到哪个函数来处理。
                    )
                    yield FormRequest
                else:
                    pass

    def parse(self, response):
        name = response.xpath("//ul[@class='bazi_box']/li[1]/text()").extract()
        birth = response.xpath("//ul[@class='bazi_box']/li[3]/text()").extract()
        sex = response.xpath("//ul[@class='bazi_box1']/li[1]/text()").extract()
        fate = response.xpath("//ul[@class='bazi_box1']/li[5]/text()").extract()
        score1 = response.xpath("//div[@class='sm_pingfen']/span[@class='df_1 left']/text()").re("['\d','\.']+")
        score2 = response.xpath("//div[@class='sm_pingfen']/span[@class='df_1 right']/text()").re("['\d','\.']+")

        #取高分
        # if int(score1[0]) >= 90 and int(score2[0]) >= 90:


        item = PostinfoItem()
        item["name"] = name
        item["birth"] = birth
        item["sex"] = sex
        item["fate"] = fate
        item["score1"] = score1
        item["score2"] = score2
        yield item