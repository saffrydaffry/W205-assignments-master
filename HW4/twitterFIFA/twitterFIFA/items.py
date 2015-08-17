# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitterfifaItem(scrapy.Item):
    #page_texts = scrapy.Field()
    #page_linktxts = scrapy.Field()
    #page_links = scrapy.Field()
    #max_id = scrapy.Field()
    #page_dates = scrapy.Field()
    tweet_texts = scrapy.Field()
    tweet_date = scrapy.Field()
    tweet_userid = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
