# -*- coding: utf-8 -*-
import scrapy


class GlassDataSpider(scrapy.Spider):
    name = 'glass_data'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
    	for product in response.xpath("//div[@class='col-sm-6 col-md-4 m-p-product']"):
    		yield {
    		'product_url' : product.xpath(".//p[@class='pname col-sm-12']/a/@href").get(),
    		'image_url' : product.xpath(".//div[@class='pimg default-image-front']/a/img[@class='angle-image']/@src").get(),
    		'product_name' : product.xpath(".//p[@class='pname col-sm-12']/a/text()").get(),
    		'product_price' : product.xpath(".//div[@class='row']/div[contains(@class,'pprice')]/span/text()").get()    		}

    	next_page = response.xpath("//ul[@class='pagination']/li[7]/a/@href").get()

    	if next_page:
    		yield  scrapy.Request (url=next_page , callback=self.parse)     
