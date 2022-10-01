import scrapy

class ShopSpider(scrapy.Spider):
    name = "nlp-spider"
    start_urls = ["https://www.beautymind.pl/"]
    custom_settings = {
        "USER_AGENT": "SeKonBot/1.0 (https://zazepa.pl/bot.html)",
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_DEBUG": True,
        "DOWNLOAD_DELAY": 1,
        "HTTPCACHE_ENABLED": True,
}
    def parse(self, response):
        for post in response.css("h3.entry-title a"):
            yield {"url": post.attrib.get('href')}
        for prev_page in response.css("a.next"):
            yield response.follow(prev_page, self.parse)