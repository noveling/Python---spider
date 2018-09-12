# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tkcrawler.items import TkcrawlerItem


class TkspiderSpider(CrawlSpider):
    name = 'tkspider'
    allowed_domains = ['lydsy.com']
    start_urls = []
    baseurl = "https://www.lydsy.com/JudgeOnline/problemset.php?page="
    for i in range(1,46):
        reurl = baseurl + str(i)
        start_urls.append(reurl)

    rules = (
        Rule(
            LinkExtractor(
                allow=(r'.+problem\.php\?id=\d+')),
            callback='parse_item',
            follow=True),
    )

    def parse_item(self, response):
        i = TkcrawlerItem()
        i["turl"] = response.url
        i["tname"] = response.xpath("//center[3]/h2/text()").re('.*?:(.*)')[0]
        i["tlimit"] = response.xpath("//center[3]/text()").re('(.*?Sec).*')[
            0] + ',  '+response.xpath("/html/body/center[3]/text()").extract()[1]
        i["tpass"] = response.xpath("//center[3]/text()").extract()[3]
        i["tsub"] = response.xpath(
            "//center[3]/text()").re('(\w+)\xa0\xa0.*')[-1]
        i["tdes"] = ''.join(
            response.xpath("//div[1][@class='content']").xpath('string(.)').extract()) + '\n'.join(
            ["https://www.lydsy.com/JudgeOnline/" + i for i in response.xpath("//div[1][@class='content']//img/@src").extract() if not i.startswith("/")]) + '\n'.join(
            ["https://www.lydsy.com" + i for i in response.xpath("//div[1][@class='content']//img/@src").extract() if i.startswith("/")]
        )

        i["tstdin"] = ''.join(
            response.xpath("//div[2][@class='content']").xpath('string(.)').extract()) + '\n'.join(
            ["https://www.lydsy.com/JudgeOnline/" + i for i in response.xpath("//div[2][@class='content']//img/@src").extract() if not i.startswith("/")]) + '\n'.join(
            ["https://www.lydsy.com" + i for i in response.xpath("//div[2][@class='content']//img/@src").extract() if i.startswith("/")]
        )
        i['tstdout'] = ''.join(
            response.xpath("//div[3][@class='content']").xpath('string(.)').extract()) + '\n'.join(
            ["https://www.lydsy.com/JudgeOnline/" + i for i in response.xpath("//div[3][@class='content']//img/@src").extract() if not i.startswith("/")]) + '\n'.join(
            ["https://www.lydsy.com" + i for i in response.xpath("//div[3][@class='content']//img/@src").extract() if i.startswith("/")])

        i["sample"] = "输入: " + ''.join(response.xpath("//div[4][@class='content']").xpath('string(.)').extract(
        )) + '\n'.join(
            ["https://www.lydsy.com/JudgeOnline/" + i for i in response.xpath("//div[4][@class='content']//img/@src").extract() if not i.startswith("/")]) + '\n'.join(
            ["https://www.lydsy.com" + i for i in response.xpath("//div[4][@class='content']//img/@src").extract() if i.startswith("/")])+"\n输出: " + ''.join(response.xpath("//div[5][@class='content']").xpath('string(.)').extract())+ '\n'.join(
            ["https://www.lydsy.com/JudgeOnline/" + i for i in response.xpath("//div[5][@class='content']//img/@src").extract() if not i.startswith("/")]) + '\n'.join(
            ["https://www.lydsy.com" + i for i in response.xpath("//div[5][@class='content']//img/@src").extract() if i.startswith("/")])
        i["source"] = '\n'.join(['https://www.lydsy.com/JudgeOnline/'+i for i in response.xpath(
            "//div[7][@class='content']/p/a/@href").extract()])
        i["data"] = ''.join(
            response.xpath("//div[6][@class='content']").xpath('string(.)').extract()) + '\n'.join(
            ["https://www.lydsy.com/JudgeOnline/" + i for i in response.xpath("//div[6][@class='content']//img/@src").extract() if not i.startswith("/")])+ '\n'.join(
            ["https://www.lydsy.com" + i for i in response.xpath("//div[6][@class='content']//img/@src").extract() if i.startswith("/")])
        yield i
