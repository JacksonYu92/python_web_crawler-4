import scrapy


class BloodSpider(scrapy.Spider):
    #爬虫文件的唯一标识
    name = "blood"
    #允许的域名
    # allowed_domains = ["www.xxx.com"]
    #起始的url列表（重要）：列表内部的url都会被框架进行异步的请求发送
    start_urls = ["https://www.xiachufang.com/category/40076/"]

    def parse(self, response):
        li_list = response.xpath('/html/body/div[4]/div/div/div[1]/div[1]/div/div[2]/div[2]/ul/li')
        for li in li_list:
            # title = li.xpath('./div/div/p[1]/a/text()')[0].extract().strip()
            title = li.xpath('./div/div/p[1]/a/text()').extract_first().strip()
            print(title)