# Scrapy settings for wangxiao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangxiao'

SPIDER_MODULES = ['wangxiao.spiders']
NEWSPIDER_MODULE = 'wangxiao.spiders'
LOG_LEVEL = 'ERROR'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wangxiao (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Cookie': '_bl_uid=Lsl8knLtznOnvnxLXi9dt3pz9m1d; mantis6894=f180d6a8a9304f81b492d86244aed1ee@6894; is-visited=true; Hm_lvt_fd91d2ffbfa83c234c1cee672a69326c=1697869955; sign=jls; pc_398265633_exam=fangchan; safedog-flow-item=; userInfo=%7B%22userName%22%3A%22pc_398265633%22%2C%22token%22%3A%224794ede6-54cf-4d74-a337-fa71f24fc0dc%22%2C%22headImg%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FPiajxSqBRaEKplN5ibkPDJd5UZyVocGN4xa9ehaIPYVVqgt36XlGzib5FJJ8o3fdvLZLebnnUX0pspOTE8XCpjCzw%2F132%22%2C%22nickName%22%3A%22189****9225%22%2C%22sign%22%3A%22fangchan%22%2C%22isBindingMobile%22%3A%221%22%2C%22isSubPa%22%3A%220%22%2C%22userNameCookies%22%3A%22lwDvjTKt%2BuW3%2BUkUBIJWvQ%3D%3D%22%2C%22passwordCookies%22%3A%22Zjaf4MyWoxw%3D%22%7D; token=4794ede6-54cf-4d74-a337-fa71f24fc0dc; UserCookieName=pc_398265633; OldUsername2=lwDvjTKt%2BuW3%2BUkUBIJWvQ%3D%3D; OldUsername=lwDvjTKt%2BuW3%2BUkUBIJWvQ%3D%3D; OldPassword=Zjaf4MyWoxw%3D; UserCookieName_=pc_398265633; OldUsername2_=lwDvjTKt%2BuW3%2BUkUBIJWvQ%3D%3D; OldUsername_=lwDvjTKt%2BuW3%2BUkUBIJWvQ%3D%3D; OldPassword_=Zjaf4MyWoxw%3D'}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wangxiao.middlewares.WangxiaoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wangxiao.middlewares.WangxiaoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wangxiao.pipelines.WangxiaoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
