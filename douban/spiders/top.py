# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
import sys

sys.path.append(r'E:\Python\pachong\scrapy\douban')

from douban.items import DoubanItem


class TopSpider(Spider):
    name = 'top'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
    	movies=response.xpath('//div[@class="info"]')
    	for movie in movies:  #用一个循环就能爬取页面里所有满足条件的节点
    		item=DoubanItem()
    		item['Name']=movie.xpath('div[@class="hd"]//span[@class="title"]/text()').extract_first()
    		item['Casts']=movie.xpath('div[@class="bd"]/p/text()').extract_first().strip()
    		item['Score']=movie.xpath('div[@class="bd"]//div[@class="star"]//span[@class="rating_num"]/text()').extract_first()
    		item['Quote']=movie.xpath('div[@class="bd"]//p[@class="quote"]//span[@class="inq"]/text()').extract_first()
    		yield item

    	next_page=response.xpath('//span[@class="next"]/link/@href').extract_first()
    	if next_page:
    		yield response.follow(next_page,callback=self.parse)