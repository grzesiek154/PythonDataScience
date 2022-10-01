import scrapy


class ShopSpider(scrapy.Spider):

    name = "shopspider"
    start_urls = ["http://www.katalogsklepowinternetowych.pl/"]
    custom_settings = {
        "USER_AGENT": "SeKonBot/1.0 (https://zazepa.pl/bot.html)",
    }

    def parse(self, response):
        for category in response.css("li>a.szary"):
            yield response.follow(category, self.parse_category_page)

    def parse_category_page(self, response):
        category = response.xpath("//span[@class = 'post-cat']/a/text()").get()
        for shop_a in response.css("img+br+br+a"):
            yield {"sklep": shop_a.attrib["href"], "kategoria": category}
        for prev_page in response.css("span.previous-entries>a"):
            yield response.follow(prev_page, self.parse_category_page)
