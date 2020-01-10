# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
    	Table= response.xpath("//table[@class='table table-striped']/tbody/tr")
    	for table in Table:
    		Name = table.xpath(".//td[1]/a/text()").get()
    		National_debt_to_GDP_ratio = table.xpath(".//td[2]/text()").get()
    		Population = table.xpath(".//td[3]/text()").get()
    		yield {
    		"Country": Name,
    		"gdp_debt":National_debt_to_GDP_ratio,
    		"Population":Population
    		} 
   
        
