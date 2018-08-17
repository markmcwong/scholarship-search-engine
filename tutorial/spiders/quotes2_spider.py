import scrapy
import html2text

class QuotesSpider(scrapy.Spider):
    name = "quotes2"

    def start_requests(self):
        start_urls = [url.strip() for url in open('tutorial/spiders/collection.txt','r')]
        print(start_urls)
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('body'):
            yield {
                'url': response.request.url,
                'scholarship': quote
            }