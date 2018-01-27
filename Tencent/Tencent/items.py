# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #name of the positon
    positionName = scrapy.Field()
    #hyper link of details of the position
    positionLink = scrapy.Field()
    #type of the position
    positionType = scrapy.Field()
    #number of requirement of the position
    requireNumber = scrapy.Field()
    #working location
    workLocation = scrapy.Field()
    #publish time
    publishTime = scrapy.Field()
