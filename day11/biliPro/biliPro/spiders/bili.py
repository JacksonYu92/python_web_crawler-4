import scrapy
from biliPro.items import BiliproItem

class BiliSpider(scrapy.Spider):
    name = "bili"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://search.bilibili.com/all?keyword=pyqt"]

    # def parse(self, response):
    #
    #     div_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[2]/div/div')
    #     # print(div_list)
    #     all_data = []
    #     for div in div_list:
    #         title = div.xpath('./div/div[2]/div/div/a/h3//text()').extract()
    #         title = ''.join(title)
    #         author = div.xpath('./div/div[2]/div/div/p/a/span[1]/text()').extract_first()
    #         # print(title, author)
    #         #持久化存储:基于终端指令(简单,局限性较大)   基于管道的形式(复杂,灵活程度高)
    #         dic = {
    #             'title': title,
    #             'author': author,
    #         }
    #         all_data.append(dic)
    #     return all_data

    #基于管道实现的持久化存储:
    def parse(self, response):

        div_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[2]/div/div')
        # print(div_list)
        all_data = []
        for div in div_list:
            title = div.xpath('./div/div[2]/div/div/a/h3//text()').extract()
            title = ''.join(title)
            author = div.xpath('./div/div[2]/div/div/p/a/span[1]/text()').extract_first()
            #创建items类型对象/容器
            item = BiliproItem()
            item['title'] = title
            item['author'] = author

            yield item

