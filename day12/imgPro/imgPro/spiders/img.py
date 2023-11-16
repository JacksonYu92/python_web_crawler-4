import scrapy
from imgPro.items import ImgproItem


class ImgSpider(scrapy.Spider):
    name = "img"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://image.so.com/zjl?sn=0&ch=copyright"]

    def parse(self, response):
        #获取图片地址将其封装到item对象中，将item对象提交给ImagesPipeline管道
        json_data = response.json()['list']
        for dic in json_data:
            img_src = dic['qhimg_url']
            title = dic['title']
            # print(img_src, title)
            item = ImgproItem()
            item['title'] = title
            item['img_src'] = img_src

            yield item