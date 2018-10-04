# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BallerItem(scrapy.Item):
	url = scrapy.Field()
	title = scrapy.Field()
	address = scrapy.Field()
	detail = scrapy.Field()
	image_urls = scrapy.Field()
	image_paths = scrapy.Field()