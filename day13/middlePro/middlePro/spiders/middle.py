import scrapy


class MiddleSpider(scrapy.Spider):
    name = "middle"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.baidu.com","https://www.sogou.com"]
    msg = '我是爬虫文件传递给中间件的消息，请接收！'
    def parse(self, response):
        pass
