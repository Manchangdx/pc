#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scrapy
from ..items import HahaItem


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for i in response.css('li.col-12'):
            item = HahaItem()
            item['name'] = i.css('a::text').extract_first().strip()
            item['update_time'] = i.xpath('.//relative-time/@datetime').extract_first()
            url = i.xpath('.//h3/a/@href').extract_first()
            request = scrapy.Request(response.urljoin(url), self.parse_repo)
            request.meta['item'] = item
            yield request
        url = response.css('div.BtnGroup a::attr(href)').extract()[-1]
        yield response.follow(url, self.parse)

    def parse_repo(self, response):
        item = response.meta['item']
        if response.css('span.num'):
            item['commits'] = response.css('li.commits span::text').extract_first()
            item['branches'] = response.css(
                               'ul.numbers-summary span::text').extract()[1]
            item['releases'] = response.css(
                               'ul.numbers-summary span::text').extract()[2]
        return item
