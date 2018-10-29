# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AngelimgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    image_urls = scrapy.Field() # 存儲圖片的url，格式爲列表
    images = scrapy.Field() # 置空，用於給圖片管道存儲數據


