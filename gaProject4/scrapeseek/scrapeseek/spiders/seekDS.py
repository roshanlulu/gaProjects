# import libraries
import scrapy
from scrapy.http import Request
from scrapy import Selector

class GiveAnyClassName(scrapy.Spider):
    # Naming ceremony of the spider
    name = 'gogetthelinks'


    # Define the start request function
    def start_requests(self):
        # Provide the list of urls that you want to parse through
        urls = [{'type': 'data-analyst', 'url':'https://www.seek.com.au/Data-Analyst-jobs/in-All-Sydney-NSW'},
                {'type': 'data-science', 'url':'https://www.seek.com.au/Data-Science-jobs/in-All-Sydney-NSW'},
                 {'type': 'business-intelligence', 'url':'https://www.seek.com.au/Business-Intelligence-jobs/in-All-Sydney-NSW'}]

        for url in urls:
            # Each request will be passed to the parse function
            request = Request(url=url['url'], callback=self.parse)
            request.meta['meta'] = url['type']
            yield request

    # Define your parse function inside your class
    def parse(self, response):
        hxs = Selector(response)
        meta = response.meta['meta']
        links = Selector(text=response.text).xpath("//a[@data-automation='jobTitle']/@href").extract()
        print(links)
        yield {
            meta: links
        }


