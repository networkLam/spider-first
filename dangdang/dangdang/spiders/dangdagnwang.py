import scrapy

from dangdang.items import DangdangItem


class DangdagnwangSpider(scrapy.Spider):
    name = "dangdagnwang"
    # 如果是多页下载的话 就必须要调整allowed_domains的范围，一般情况下只写域名
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.03.30.00.00.00.html"]
    page = 1
    base_url = "https://category.dangdang.com/pg"
    def parse(self, response):
        li_list = response.xpath(" //div[@id='search_nature_rg']//li")
        # print(li_list)
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath(".//img/@src").extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[@class="search_now_price"]/text()').extract_first()
            print(src, name, price)
            book = DangdangItem(src=src, name=name, price=price)
            # 每得到一个book 就把book给pipelines处理
            yield book

        if self.page < 10:
            self.page = self.page + 1
            #https://category.dangdang.com/pg2-cp01.03.30.00.00.00.html
            # https://category.dangdang.com/pg3-cp01.03.30.00.00.00.html
            url = self.base_url + str(self.page) + "-cp01.03.30.00.00.00.html"
            # scrapy.Request 就是scrapy的get请求
            yield scrapy.Request(url=url,callback=self.parse)
        pass
