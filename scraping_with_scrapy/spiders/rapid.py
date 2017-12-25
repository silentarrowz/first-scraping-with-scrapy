# -*- coding: utf-8 -*-
import scrapy


class RapidSpider(scrapy.Spider):
    name = 'rapid'
    allowed_domains = ['https://rapidapi.com']
    start_urls = ['https://rapidapi.com/']

    def parse(self, response):
       # apis = response.xpath('//span[@class="_3FG7l"]/text()').extract()
        catgs = response.xpath('//li[@class="gg5W7"]/a[@href]/text()').extract()
       # for api in apis:
        #	yield {'title':api}
       # print(catgs)
        for catg in catgs:
        	yield {'catgs':catg}