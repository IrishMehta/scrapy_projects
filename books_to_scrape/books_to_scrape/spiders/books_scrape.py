# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksScrapeSpider(CrawlSpider):
    name = 'books_scrape'
    allowed_domains = ['books.toscrape.com']


    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'


    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']/article/h3/a"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="(//li[@class='next']/a)"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'Book Name': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'Price': response.xpath("//div[@class='col-sm-6 product_main']/p[@class='price_color']/text()").get(),
            
        }
