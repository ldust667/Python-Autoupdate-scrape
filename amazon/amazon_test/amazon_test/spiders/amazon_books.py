# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonTestItem

class AmazonBooksSpider(scrapy.Spider):
    name = 'amazon_books'
    start_urls = ['http://amazon.com/']

    def parse(self, response):
	items = AmazonTestItem()
	#will normally extract html this is changing it to text
	product_name = response.css('.s-access-title::text').extract()
	items['product_name'] = product_name
	yield items
        
