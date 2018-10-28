# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# scrapy genspider -t crawl angelspider www.angelimg.com  
class AngelspiderSpider(CrawlSpider):
    name = 'angelspider'
    allowed_domains = ['angelimg.com']
    start_urls = ['http://www.angelimg.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.angelimg.com/index/\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print(response.url)
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
