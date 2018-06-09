# -*- coding: utf-8 -*-
import scrapy
from haha.items import HahaItem


class ASpider(scrapy.Spider):
    name = 'a'
    url = 'https://github.com/shiyanlou?page={}&tab=repositories'
    start_urls = (__class__.url.format(i) for i in range(1, 5))

    def parse(self, response):
        for i in response.css('li.col-12'):
            item = HahaItem({
                'name': i.css('a::text').extract_first().strip(),
                'update_time': i.css('relative-time::attr(datetime)').extract_first()
            })
            url = i.css('a::attr(href)').extract_first()
            r = scrapy.Request(url=response.urljoin(url), callback=self.haha)
            r.meta['item'] = item
            yield r

    def haha(self, response):
        item = response.meta['item']
        if not response.css('span.num::text').extract()[0]:
            pass
        else:
            item['commits'] = response.css('span.num::text').extract()[0].strip()
            item['branches'] = response.css('span.num::text').extract()[1].strip()
            item['releases'] = response.css('span.num::text').extract()[2].strip()
            yield item
