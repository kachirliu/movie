# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    Name=scrapy.Field()
    Casts=scrapy.Field()
    Score=scrapy.Field()
    Quote=scrapy.Field()
