# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ScrapeToFileSpider(scrapy.Spider):
    name = 'crawl-tofile-xpath'
    start_urls = [
        'http://www.planecrashinfo.com/1920/1920-1.htm'
    ]

    def parse(self, response):
        filename = 'crawl_tofile.csv'
        with open(filename, 'a') as f:
            for column_name, content in zip(response.xpath('//b/text()'), response.xpath('//td/font/text()')):
                f.write(column_name.extract())
                f.write(content.extract())
                f.write('\n')
            f.write('\n\n')
        f.close()


