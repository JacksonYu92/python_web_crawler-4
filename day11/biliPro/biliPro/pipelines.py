# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BiliproPipeline:
    fp = None
    def open_spider(self, item):
        print('文件创建成功')
        self.fp = open('bili.txt', 'w')
    def close_spider(self, item):
        self.fp.close()
        print('文件关闭成功!')
    def process_item(self, item, spider):
        print(item)
        title = item['title']
        author = item['author']
        self.fp.write(author+':'+title+'\n')
        print(title,': 写入文件成功!')
        return item
