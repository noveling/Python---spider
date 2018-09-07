# -*- coding: utf-8 -*-

# Scrapy settings for ajaxdouban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ajaxdouban'

SPIDER_MODULES = ['ajaxdouban.spiders']
NEWSPIDER_MODULE = 'ajaxdouban.spiders'

COOKIE = {'bid': 'wJCjssl5Les', 'douban-fav-remind': '1', '__yadk_uid': 'WxTqJrsNwoKxt9zl8kajXBdp81P8PpIj', 'ps': 'y', 'll': '"118254"', 'viewed': '"3823020_1058458_3361748_26886310_26895119"', 'gr_user_id': '8d7c2126-2584-4422-b851-d1f0784a9a52', '_vwo_uuid_v2': 'D120E731276483A105142A5B5EF80FEF0|ff4b53d36575c38201ac93f466ede2bb', '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1536211950%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPeOBC6r-rhweGMLUlGbzYICsuffnoGyLfD5M4CkfAW2nA0JCazHX6yliwSO_o7Ju%26wd%3D%26eqid%3D94b96202000104af000000055b90bc06%22%5D', '__utmt': '1', 'ap_v': '0,6.0', 'push_noty_num': '0', 'push_doumail_num': '0', '__utma': '30149280.504159862.1532070102.1535946949.1536211954.14', '__utmb': '30149280.6.10.1536211954', '__utmc': '30149280', '__utmz': '30149280.1536211954.14.8.utmcsr', '__utmv': '30149280.18416', 'dbcl2': '"184168299:XCr2G6+ARK4"', '_ga': 'GA1.2.504159862.1532070102', '_gid': 'GA1.2.180686065.1536212470', '_gat_UA-7019765-1': '1', 'ck': '0P3m', '_pk_id.100001.8cb4': '4e26cf9c720db1b8.1532070100.10.1536212472.1535946950.', '_pk_ses.100001.8cb4': '*'}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

DOWNLOAD_DELAY = 0.5

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ajaxdouban (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ajaxdouban.middlewares.AjaxdoubanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ajaxdouban.middlewares.AjaxdoubanDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'ajaxdouban.pipelines.AjaxdoubanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
