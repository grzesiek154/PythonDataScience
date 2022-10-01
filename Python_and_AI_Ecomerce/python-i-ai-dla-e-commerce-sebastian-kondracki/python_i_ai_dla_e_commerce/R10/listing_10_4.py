import scrapy

class ShopSpider(scrapy.Spider):
    name = 'shopspider'
    start_urls = ['http://www.katalogsklepowinternetowych.pl/']
    custom_settings = {
        'USER_AGENT' : 'SeKonBot/1.0 (https://zazepa.pl/bot.html)',
    }
    
    def parse(self, response):
        for shop_a in response.css('img+br+br+a'):
            yield {'sklep': shop_a.attrib['href']}
        for prev_page in response.css('span.previous-entries>a'):
            yield response.follow(prev_page, self.parse)