# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    # allowed_domains = ['https:\www.myntra.com']
    # start_urls = ['http://https:\www.myntra.com/']
    
    def __init__(self):
        self.page = "https://www.myntra.com"
    
    def start_requests(self):
        yield SplashRequest(
            url="https://www.myntra.com",
            callback=self.parse
        )
        
    def data_pages(self,response):
        # brands = response.xpath("//h3[@class='product-brand]")
        # print(brands)
        
        #print("****************************\n\n\n",response.url,"\n\n\n*********************************")
        print("***********************")
    def sub_pages(self,response):
        #print("****************************\n\n\n",response.url,"\n\n\n*********************************")
        links = response.xpath("//a[@class='navi-link navi-underline']/@href").extract()
        print(links)
        
        for link in links:
            yield SplashRequest(url=self.page+link,callback=self.data_pages)
            
    def parse(self, response):
        links = response.xpath("//a[@class='desktop-main']/@href").extract()
        
        for link in links:
            yield SplashRequest(url=self.page+link,callback=self.sub_pages,
                                args={
        # optional; parameters passed to Splash HTTP API
        'wait': 1,

        # 'url' is prefilled from request url
        # 'http_method' is set to 'POST' for POST requests
        # 'body' is set to request body for POST requests
    }
                                )
        pass
