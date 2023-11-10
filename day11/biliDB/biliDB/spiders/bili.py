import scrapy
from biliDB.items import BilidbItem

class BiliSpider(scrapy.Spider):
    name = "bili"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://search.bilibili.com/all?keyword=pyqt"]

    def parse(self, response):
        div_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[2]/div/div')
        # print(div_list)
        all_data = []
        for div in div_list:
            title = div.xpath('./div/div[2]/div/div/a/h3//text()').extract()
            title = ''.join(title)
            author = div.xpath('./div/div[2]/div/div/p/a/span[1]/text()').extract_first()
            # 创建items类型对象/容器
            item = BilidbItem()
            item['title'] = title
            item['author'] = author

            yield item
