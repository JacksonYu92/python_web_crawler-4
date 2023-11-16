# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

class ImgproPipeline(ImagesPipeline):
    #三个固定函数
    def get_media_requests(self, item, info):
        #该函数是负责对图片进行请求发送获取图片二进制的数据
        #可以通过item参数接收爬虫文件提交过来的item对象
        title = item["title"]
        img_src = item["img_src"]

        #对图片地址进行请求发送（手动发起请求）
        #meta参数：实现请求传参
        yield scrapy.Request(img_src,meta={"title":title})

    #负责指定保存图片时图片的名字
    def file_path(self, request, response=None, info=None, *, item=None):
        #获取图片名字
        title = request.meta['title']+'.jpg'
        print(title, "爬取保存成功！")
        return title

    def item_completed(self, results, item, info):
        return item
