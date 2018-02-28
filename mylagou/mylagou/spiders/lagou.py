# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com/jobs/list_python']
    start_urls = ['http://www.lagou.com/jobs/list_python/']

    def parse(self, response):
        print("--------------------------")
        for item in response.css(".item_con_list first_row default_list"):
            print("**************")
            companyname=item.xpath("data-salary/text()").extract()
            print(companyname)