# -*- coding: utf-8 -*-
import scrapy


class uiucEventbriteSpider(scrapy.Spider):
    name = "eventbrite"
    allowed_domains = ["eventbrite.com"]
    start_urls = (
        'https://www.eventbrite.com/d/il--champaign/events/?crt=regular&sort=date','https://www.eventbrite.com/d/il--urbana/events/?crt=regular&sort=date'
    )

    def parse(self, response):
        pass
