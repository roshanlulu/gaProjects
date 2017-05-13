# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class myFirstSpider(scrapy.Spider):
    name = 'crawl-1-xpath'
    start_urls = [
        'http://www.planecrashinfo.com/1920/1920-1.htm'
        'http://www.planecrashinfo.com/1920/1920-2.htm',
        'http://www.planecrashinfo.com/1920/1920-3.htm',
        'http://www.planecrashinfo.com/1920/1920-4.htm'
    ]


    def parse(self, response):
        yield {
            response.xpath('//b/text()').extract()[0]:response.xpath('//td/font/text()').extract()[0],
            response.xpath('//b/text()').extract()[1]: response.xpath('//td/font/text()').extract()[1]
        }

        # for column_name, content in zip(response.xpath('//b/text()'), response.xpath('//td/font/text()')):
        #     yield {
        #         column_name.extract():content.extract()
        #     }
