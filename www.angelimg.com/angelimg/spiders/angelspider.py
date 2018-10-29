'''
www.angelimg.com
    www.angelimg.com/\d+,首頁翻頁 不做回調處理，取翻頁的url
    
    從首頁翻頁的響應中，提取圖集的列表頁面，是否需要回調？
    www.angelimg.com/ang/\d+ 很多個圖集，不需要回調，取翻頁的url
    
    www.angelimg.com/1440/\d+,圖集翻頁，做回調處理，分析並提取網頁中的圖片url，提供下載用

    規則倒寫
'''

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AngelimgItem
from scrapy.pipelines.images import ImagesPipeline

# scrapy genspider -t crawl angelspider www.angelimg.com  
class AngelspiderSpider(CrawlSpider):
    name = 'angelspider'
    allowed_domains = ['angelimg.com']
    #start_urls = ['http://www.angelimg.com/']
    start_urls = ['http://www.angelimg.com/ang/1440']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.angelimg.com/ang/\d+/\d+'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'http://www.angelimg.com/ang/\d+'),  follow=True),
        #Rule(LinkExtractor(allow=r'http://www.angelimg.com/index/\d+'), follow=True),
    )

    def parse_item(self, response):
        #print(response.url,'------')
        item = AngelimgItem()
        item['image_urls'] = response.xpath('.//div[@id="content"]//img/@src').extract()
        #print(item,'------')
        yield item
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
