# -*- coding: utf-8 -*-
import scrapy

from larsen_delpeterson.items import LarsenDelpetersonItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class DelpetersonSpider(scrapy.Spider):
    name = 'delpeterson'
    allowed_domains = ['delpeterson.com']
    base_url = 'https://www.delpeterson.com/servlet/Search.do?auctionId={}&keyword=&categoryName=&page=1&noCache=false&perPage=9999'

    def __init__(self, auction_id='', **kwargs):
        self.auction_id = auction_id
        self.start_urls = [self.base_url.format(auction_id)]
        super(DelpetersonSpider, self).__init__(**kwargs)

    def parse(self, response):
        lots = response.xpath('//td[@width="448"]/a[contains(@href, "itemId")]')
        for lot in lots:
            yield response.follow(lot, callback=self.parse_lot)

    def parse_lot(self, response):

        l = ItemLoader(item=LarsenDelpetersonItem(), response=response)
        l.default_output_processor = TakeFirst()

        l.add_xpath('LotNum', '//h1/text()')
        l.add_xpath('LotDescription', '//h2[contains(text(), "Item Details:")]/following-sibling::p[1]/text()[1]')

        address = response.xpath('//b[contains(text(), "Item Location:")]/following-sibling::text()[1]').extract_first()
        city, region = address.split(',')
        l._add_value('City', city)
        l._add_value('State', region)
        l._add_value('ZIP', region)
        l.add_xpath('Contact', '//b[contains(text(), "Equipment Contact:")]/following-sibling::text()[1]')
        l.add_xpath('Phone', '//b[contains(text(), "Phone Number:")]/following-sibling::text()[1]')
        l.add_xpath('Category', '//strong[contains(text(), "Category:")]/following-sibling::text()[1]')
        l.add_xpath('ClosesOn', '//strong[contains(text(), "Closes On")]/following-sibling::text()[1]')
        l.add_xpath('image_urls', '//div[@id="gallery"]//a/@href')
        l.add_value('folder_name', self.auction_id)

        yield l.load_item()
