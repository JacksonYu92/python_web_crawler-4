# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline

class FileproPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        file_urls = item['file_urls']
        file_name = item['file_name']
        yield scrapy.Request(file_urls, meta={'file_name': file_name})

    def file_path(self, request, response=None, info=None, *, item=None):
        fileName = request.meta['file_name']
        print(fileName, '下载保存成功！')
        return fileName

    def item_completed(self, results, item, info):
        return item