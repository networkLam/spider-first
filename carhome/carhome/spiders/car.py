import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    # 如果请求的接口结尾是html的，后缀不能加/ 否则就会请求失败
    start_urls = ["https://car.autohome.com.cn/price/brand-75-146.html"]

    def parse(self, response):
        name_list = response.xpath('//*[@class="main-title"]/a/text()')
        price_list = response.xpath('//span[@class="font-arial"]/text()')
        # print(price_list)
        # print(name_list)
        for item in range(len(name_list)):
            name = name_list[item].extract()
            price = price_list[item].extract()
            print(name, price)
        # print("=====这个是测试======")
        # print("=====这个是测试======")
        # print("=====这个是测试======")
        pass
