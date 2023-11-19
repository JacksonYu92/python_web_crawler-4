import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    # allowed_domains = ["www.x.com"]
    start_urls = ["https://news.163.com/"]
    model_url_list = []
    # 创建一个浏览器对象
    bro = webdriver.Chrome()

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        li_list = li_list[1:3]
        for li in li_list:
            model_url = li.xpath('./a/@href').extract_first()
            self.model_url_list.append(model_url)
            yield scrapy.Request(url=model_url, callback=self.model_parse)

    def model_parse(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            item = WangyiproItem()
            item['title'] = title
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={"item":item})

    def parse_detail(self, response):
        item = response.meta['item']
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item['content'] = content
        yield item

    def closed(self, spider):
        print('整个操作结束！！！')
        self.bro.quit()