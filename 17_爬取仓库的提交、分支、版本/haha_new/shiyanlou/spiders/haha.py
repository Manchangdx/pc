# -*- coding: utf-8 -*-
import scrapy
from ..items import ShiyanlouItem

class HahaSpider(scrapy.Spider):
    name = 'haha'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for i in response.css('li.col-12'):
            item = ShiyanlouItem(update_time=i.xpath('.//relative-time/@datetime').extract_first())
            url = i.css('a::attr(href)').extract_first()
            request = scrapy.Request(response.urljoin(url), callback=self.after_parse)
            request.meta['item'] = item
            yield request
        url = response.css('div.pagination a')[-1].css('::attr(href)').extract_first()
        yield response.follow(url, callback=self.parse)

    def after_parse(self, response):
        item = response.meta['item']
        if response.css('span.num'):
            item['name'] = response.xpath('//strong[@itemprop="name"]/a/text()').extract_first()
            item['commits'] = response.css('span.num::text').extract()[0].strip()
            item['branches'] = response.css('span.num::text').extract()[1].strip()
            item['releases'] = response.css('span.num::text').extract()[2].strip()
        yield item
