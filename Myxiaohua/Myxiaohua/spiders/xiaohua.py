# -*- coding: utf-8 -*-
import scrapy
import os

from Myxiaohua.items import MyxiaohuaItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['www.xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']
    def parse(self, response):
        allPics = response.xpath('//div[@class="img"]/a')
        for pic in allPics:
            # 分别处理每个图片，取出名称及地址
            item = MyxiaohuaItem()
            name = pic.xpath('./img/@alt').extract()[0]
            addr = pic.xpath('./img/@src').extract()[0]
            addr = 'http://www.xiaohuar.com'+addr
            item['name'] = name
            item['addr'] = addr
            # 返回爬取到的数据
            yield item
        
        url=response.xpath("//div[@class='page_num']/a[17]/@href").extract();
        print(url)
        print(type(url))
        yield scrapy.Request(str(url),callback=self.parse)

