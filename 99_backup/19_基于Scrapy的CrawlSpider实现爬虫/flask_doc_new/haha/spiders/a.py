import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from ..items import HahaItem

class Haha(CrawlSpider):
    name = 'haha'
    start_urls = ['http://flask.pocoo.org/docs/1.0/']
    rules = (
        Rule(
            LinkExtractor(allow='http://flask.pocoo.org/docs/1.0/*'),
            callback='parse_item',
            follow=True
        ),
    )

    def parse_item(self, response):
        yield HahaItem(
            url = response.url,
            text = ' '.join(response.css('::text').extract())
        )
