# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DeepproItem(scrapy.Item):
    # define the fields for your item here like:
    state = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
