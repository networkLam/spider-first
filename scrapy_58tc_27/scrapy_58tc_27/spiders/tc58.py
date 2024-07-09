import scrapy


class Tc58Spider(scrapy.Spider):
    name = "tc58"
    allowed_domains = ["gz.58.com"]
    start_urls = ["https://gz.58.com/minsuduanzu/"]

    def parse(self, response):
        print(response.text)
        pass
