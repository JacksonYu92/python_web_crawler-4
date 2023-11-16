import scrapy


class PostSpider(scrapy.Spider):
    name = "post"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://fanyi.baidu.com/sug"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, callback=self.parse,formdata={'kw':'cat'})

    def parse(self, response):
        ret = response.json()
        print(ret)
