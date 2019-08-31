# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MycrawlItem(scrapy.Item):
    guanzhu = scrapy.Field()
    fensi = scrapy.Field()
    weiboshu = scrapy.Field()
    link = scrapy.Field()
    jibeninfo = scrapy.Field()
    lianxiinfo = scrapy.Field()
    taginfo = scrapy.Field()
    jobinfo = scrapy.Field()
    jyinfo = scrapy.Field()
