# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义数据结构
class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # note:
    # name is book name
    # scr is book cover
    # price is book price
    name = scrapy.Field()
    src = scrapy.Field()
    price = scrapy.Field()


    pass
