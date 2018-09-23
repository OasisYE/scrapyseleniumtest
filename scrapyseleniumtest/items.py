# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy import Item, Field


# class ScrapyseleniumtestItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

# 定义信息封装类（图片、价格、评价人数、标题、店铺名称）
class ProductItem(scrapy.Item):

    collection = 'products'

    # image = scrapy.Field()
    # price = scrapy.Field()
    # deal = scrapy.Field()
    # title = scrapy.Field()
    # shop = scrapy.Field()
    # location = scrapy.Field()

    image = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    shop = scrapy.Field()
    commit = scrapy.Field()
