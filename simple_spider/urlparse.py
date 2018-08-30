import re
import urllib.parse as urlparse
from bs4 import BeautifulSoup


class HtmlParser:

    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,"lxml")
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        print(new_data)
        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',attrs={"href":re.compile(r'^/item/.*',re.S)})
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = dict()
        data['url'] = page_url
        title = soup.find("title").string
        data["title"] = title
        return data