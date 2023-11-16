import scrapy

from filePro.items import FileproItem
class FileSpider(scrapy.Spider):
    name = "file"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://docs.twistedmatrix.com/en/stable/core/examples/"]

    def parse(self, response):
        li_list = response.xpath('//*[@id="echo-server-client-variants"]/ul/li')
        for li in li_list:
            file_url = li.xpath('./p/a/@href').extract_first()
            file_url = file_url.split('../../')[-1]
            file_url = 'https://docs.twistedmatrix.com/en/stable/' + file_url

            file_name = li.xpath('./p/a/code/span/text()').extract_first()
            # print(file_name,file_url)

            item = FileproItem()
            item['file_name'] = file_name
            item['file_urls'] = file_url

            yield item
