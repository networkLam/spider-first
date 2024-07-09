import scrapy

from ddtt.items import DdttItem
# 爬取电影天堂的内容

class Ddtd8Spider(scrapy.Spider):
    name = "ddtd8"
    allowed_domains = ["ygdy8.net"]
    start_urls = ["https://ygdy8.net/html/gndy/china/index.html"]

    def parse(self, response):
        print("============")
        # 获取整个a元素
        link_list = response.xpath("//table[@class='tbspan']//b//a[@class='ulink'][2]")
        for link in link_list:
            name = link.xpath("./text()").extract_first()
            href = link.xpath("./@href").extract_first()
            print(name, href)
            # 第二页链接
            url = "https://ygdy8.net" + href
            # movie = DdttItem(name=name, src=url)
            yield scrapy.Request(url=url, callback=self.parse_second, meta={"name": name})

        pass

    def parse_second(self, response):
        name = response.meta['name']
        # //div[@id='Zoom']//img/@src
        src = response.xpath("//div[@id='Zoom']//img/@src").extract_first()
        movie = DdttItem(name=name, src=src)

        yield movie
