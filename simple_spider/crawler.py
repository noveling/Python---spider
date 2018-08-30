from urldownload import HtmlDownloader
from urlmanage import Urlmanager
from urlparse import HtmlParser
from storedata import DataOutput


class SpiderMan:
    def __init__(self):
        self.manager = Urlmanager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            new_url = self.manager.get_new_url()
            html = self.downloader.download(new_url)
            new_url, data = self.parser.parser(new_url, html)
            for url in new_url:
                self.manager.add_new_url(url)
            self.output.store_data(data)
        self.output.output_html()

        print(self.manager.old_url_size())


if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/12/1016")
