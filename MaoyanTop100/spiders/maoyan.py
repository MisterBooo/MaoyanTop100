# -*- coding: utf-8 -*-
import scrapy
import re
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['http://maoyan.com/board/4']
    start_urls = ['http://maoyan.com/board/4/']

    def parse(self, response):

        contents = response.css('div.board-item-content')
        for content in contents:
            info = content.css('div.movie-item-info')
            name = info.css('[data-act=boarditem-click]::text').extract_first(default='not-found')
            star = info.css('p.star::text').extract_first(default='not-found').strip()
            releasetime = info.css('p.releasetime::text').extract_first(default='not-found')
            score = content.css('div.movie-item-number')
            integer = score.css('i.integer::text').extract_first()
            fraction = score.css('i.fraction::text').extract_first()
            print(name, star, releasetime,integer + fraction)



        pass
