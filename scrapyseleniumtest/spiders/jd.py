# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from urllib.parse import quote
from scrapyseleniumtest.items import ProductItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    base_url = 'https://list.jd.com/list.html?cat=670,671,672'

    def start_requests(self):
        '''遍历爬取所有页面'''
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            yield scrapy.Request(url=self.base_url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        # 获取本页面下所有商品信息
        products = response.css('ul.gl-warp li')
        for product in products:
            item = ProductItem()
            item['name'] = product.css('div.p-name a em::text').extract_first().strip()
            item['price'] = product.css('div.p-price strong.J_price i::text').extract_first()
            item['shop'] = product.css('div.p-shop span a::attr(title)').extract_first()
            item['commit'] = product.css('strong a.comment::text').extract_first()
            #item['image'] = 'https:' + str(product.css('div.p-img a img::attr(src)').extract_first().strip())
            #item['image'] = ''.join(product.xpath('.//div[@class="p-img"]/a/img/@src').extract()).strip()

            if product.xpath('.//div[@class="p-img"]/a/img/@src').extract_first() != None:
                item['image'] = product.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            else:
                item['image'] = product.xpath('.//div[@class="p-img"]/a/img/@data-lazy-img').extract_first()


            yield item



