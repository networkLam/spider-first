# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request


class DangdangPipeline:
    # 爬虫启动时自动运行
    def open_spider(self, spider):
        print("+++++++++++++++")
        self.fp = open("book.json", "a", encoding="utf-8")
        self.fp.write("[")

    # 处理 item 就是 yield 后面的book
    def process_item(self, item, spider):
        self.fp.write(str(item))
        self.fp.write(",")
        return item

    # 爬虫结束时运行
    def close_spider(self, spider):
        print("----------------")
        self.fp.write("]")
        self.fp.close()


# 开启多条管道
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = "http:" + item.get("src")
        filename = "./dangdang/books/" + item.get("name") + ".jpg"
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
