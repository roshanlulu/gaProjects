

# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class myFirstSpider(scrapy.Spider):
    name = 'new'
    start_urls = [
        'http://aviation-safety.net/database/record.php?id=20170102-0'
    ]


    def parse(self, response):
        # Get each column value of that data point using scrapy Selector
        a = Selector(text=response.text).xpath("//td[@class='desc']/text()").extract()[0]
        b = Selector(text=response.text).xpath("//td[@class='desc']/text()").extract()[1]
        c = Selector(text=response.text).xpath("//td[@class='desc']/text()").extract()[2]
        d = Selector(text=response.text).xpath("//td[@class='desc']/text()").extract()[3]
        e = Selector(text=response.text).xpath("//td[@class='desc']/text()").extract()[4]
        f = Selector(text=response.text).xpath("//td[@class='desc']/text()").extract()[5]

        # time = Selector(text=response.text).xpath('//td/font/text()').extract()[1]
        # location = Selector(text=response.text).xpath('//td/font/text()').extract()[2]
        # operator = Selector(text=response.text).xpath('//td/font/text()').extract()[3]
        # flight = Selector(text=response.text).xpath('//td/font/text()').extract()[4]
        # route = Selector(text=response.text).xpath('//td/font/text()').extract()[5]
        # actype = Selector(text=response.text).xpath('//td/font/text()').extract()[6]
        # reg = Selector(text=response.text).xpath('//td/font/text()').extract()[7]
        # cn_ln = Selector(text=response.text).xpath('//td/font/text()').extract()[8]
        # aboard = Selector(text=response.text).xpath('//td/font/text()').extract()[9]
        # fatalities = Selector(text=response.text).xpath('//td/font/text()').extract()[10]
        # ground = Selector(text=response.text).xpath('//td/font/text()').extract()[11]
        # summary = Selector(text=response.text).xpath('//td/font/text()').extract()[12]

        yield {
                'a':a,
                'b':b,
                'c':c,
                'd':d,
                'e':e,
                'f':f
        }

        # for column_name, content in zip(response.xpath('//b/text()'), response.xpath('//td/font/text()')):
        #     yield {
        #         column_name.extract():content.extract()
        #     }
