# -*- coding: utf-8 -*-
import scrapy


class RentmojoDataSpider(scrapy.Spider):
    name = 'rentmojo_data'
    allowed_domains = ['www.rentomojo.com']
    start_urls = ['https://www.rentomojo.com/mumbai/electronics/smartphones-on-rent']

    def parse(self, response):
    	products = response.xpath("//div[@class='col-xs-6 col-sm-4 col-mgbtm']")
    	for product in products:
    		yield { 
    			"Product name": product.xpath("normalize-space(.//h2[@class='cat-item--title1 ma-0'])").get(),
    			"Link": response.follow(url=product.xpath(".//a/@href").get() , callback=self.parse)
    			}
        
