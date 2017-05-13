# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'crawl-all-xpath'
    # Generate my start_urls
    gen_names = [('http://www.planecrashinfo.com/'+str(year)+'/'+str(year)+'-'+str(page)+'.htm')
                 for year in range(1920,2018)
                 for page in range(1,200)]
    start_urls = gen_names


    def parse(self, response):
        # Get each column value of that data point using scrapy Selector
        date = Selector(text=response.text).xpath('//td/font/text()').extract()[0]
        time = Selector(text=response.text).xpath('//td/font/text()').extract()[1]
        location = Selector(text=response.text).xpath('//td/font/text()').extract()[2]
        operator = Selector(text=response.text).xpath('//td/font/text()').extract()[3]
        flight = Selector(text=response.text).xpath('//td/font/text()').extract()[4]
        route = Selector(text=response.text).xpath('//td/font/text()').extract()[5]
        actype = Selector(text=response.text).xpath('//td/font/text()').extract()[6]
        reg = Selector(text=response.text).xpath('//td/font/text()').extract()[7]
        cn_ln = Selector(text=response.text).xpath('//td/font/text()').extract()[8]
        aboard = Selector(text=response.text).xpath('//td/font/text()').extract()[9]
        fatalities = Selector(text=response.text).xpath('//td/font/text()').extract()[10]
        ground = Selector(text=response.text).xpath('//td/font/text()').extract()[11]
        summary = Selector(text=response.text).xpath('//td/font/text()').extract()[12]

        # Next step: Get the data output to a file.
        # NOTE: The yield only supports certain formats. One is a dictionary format.
        # Yield content is displayed in your terminal.
        #  if an output file is specified then yield will be copied to the file as well.
        # Command to call your spider
        # `scrapy crawl <spider-name>
        # `scrapy crawl <spider-name> -o <filename>
        yield {
                'Date':date,
                'Time':time,
                'Location':location,
                'operator':operator,
                'Flight':flight,
                'Route':route,
                'AcType':actype,
                'Reg':reg,
                'CnLn':cn_ln,
                'Aboard':aboard,
                'Fatalities':fatalities,
                'Ground:':ground,
                'Summary':summary
        }