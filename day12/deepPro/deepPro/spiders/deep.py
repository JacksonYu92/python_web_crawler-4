import scrapy
from deepPro.items import DeepproItem


class DeepSpider(scrapy.Spider):
    name = "deep"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://wz.sun0769.com/political/index/politicsNewest"]

    #1. 定义一个通用的url模板（用来生成不同的页码链接）
    url_model = 'https://wz.sun0769.com/political/index/politicsNewest?id=1&page=%d'
    page_num = 2


    def parse(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            state = li.xpath('./span[2]/text()').extract_first().strip()
            title = li.xpath('./span[3]/a/text()').extract_first()

            item = DeepproItem()
            item['state'] = state
            item['title'] = title

            detail_url = 'https://wz.sun0769.com' + li.xpath('./span[3]/a/@href').extract_first()
            # print(state,title,detail_url)
            # callback参数：用于指定一个数据解析的回调函数
            # 使用meta请求传参的机制，将item传递给parse_detail
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        if self.page_num <= 3:
            print('正在爬取第%d页的数据......'%self.page_num)
            page_url = format(self.url_model % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=page_url, callback=self.parse)

    # 专门对详情页的url进行数据解析
    def parse_detail(self, response):
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]//text()').extract()
        content = ''.join(content).strip()

        item = response.meta['item']
        item['content'] = content
        yield item