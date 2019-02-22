#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import re
import config
import time
import chinese_to_arabic
import isnumber

class QuotesSpider(scrapy.Spider):

    name = 'quotes'
    start_urls = [config.url,
    ]

    def parse(self, response):
        for quote in response.css('dd'):
            next_page = response.urljoin(quote.css('a::attr(href)').get())
            yield response.follow(next_page, self.next_parse)
    
    def next_parse(self, response):
        try:
            re.findall(".*第(.*)章.*",response.css('div.bookname h1::text').get())[0]
            if isnumber.is_number(re.findall(".*第(.*)章.*",response.css('div.bookname h1::text').get())[0]):
                yield {
                    'title': response.css('div.bookname h1::text').get(),
                    'text': response.xpath('//div[@id="content"]').getall(),
                    'sorted': re.findall(".*第(.*)章.*",response.css('div.bookname h1::text').get())[0]
                }
            else:
                yield {
                    'title': response.css('div.bookname h1::text').get(),
                    'text': response.xpath('//div[@id="content"]').getall(),
                    'sorted': chinese_to_arabic.chinese_to_arabic(re.findall(".*第(.*)章.*",response.css('div.bookname h1::text').get())[0])
                }
            pass
        except Exception as e:
            try:
                if len(response.css('div.bookname h1::text').get().split('、')) > 2 & isnumber.is_number(response.css('div.bookname h1::text').get().split('、')[0]):
                    yield {
                        'title': response.css('div.bookname h1::text').get(),
                        'text': response.xpath('//div[@id="content"]').getall(),
                        'sorted': response.css('div.bookname h1::text').get().split('、')[0]
                    }
                pass
            except Exception as e:
                raise e
