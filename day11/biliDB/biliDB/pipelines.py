# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BilidbPipeline:
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
        self.fp.write(author + ':' + title + '\n')
        print(title, ': 写入文件成功!')
        return item

# 将数据存储到MySQL
import pymysql
class MysqlPipeLine:
    conn = pymysql.Connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        password='root',
        db='spider',
    )

    cursor = conn.cursor()

    def process_item(self, item, spider):
        title = item['title']
        author = item['author']
        sql = 'insert into bili values("%s", "%s")'%(title,author)
        self.cursor.execute(sql)
        self.conn.commit()
        # print('一条数据存储到mysql中')
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


# 将数据存储到redis
from redis import Redis #pip install redis==2.10.6
class RedisPipeLine:
    #创建链接对象
    conn = Redis(host='127.0.0.1',port=6379)
    def process_item(self, item, spider):
        #将item这个字典存储到redis中
        self.conn.lpush('bili',item)
        #lpush(参数1，参数2)：参数1新建列表的名称，参数2是向列表中存储的数据
        print('一条数据插入成功')
        return item
