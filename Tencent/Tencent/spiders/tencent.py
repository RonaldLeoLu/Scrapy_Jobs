# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    base_url = 'http://hr.tencent.com/position.php?keywords=&tid=0&lid=2175&start='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        
        for node in node_list:
            item = TencentItem()

            item['positionName'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = node.xpath('./td[1]/a/@href').extract()[0]
            if len(node.xpath('./td[2]/text()').extract()) != 0:
                item['positionType'] = node.xpath('./td[2]/text()').extract()[0]
            else:
                item['positionType'] = 'null'
            item['requireNumber'] = node.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = node.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = node.xpath('./td[5]/text()').extract()[0]

            yield item

        if len(response.xpath("//a[@class='noactive' and @id='next']")) == 0:
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            whole_url = 'http://hr.tencent.com/' + url

            yield scrapy.Request(whole_url,callback = self.parse)