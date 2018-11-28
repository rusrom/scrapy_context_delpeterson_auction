# -*- coding: utf-8 -*-

import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity


def absolute_url(url, loader_context):
    return loader_context['response'].urljoin(url)


def clear_image_url(value):
    return re.sub(r'\?.+$', '', value)


def delete_multiple_whitespaces(value):
    return re.sub(r'\s{2,}', ' ', value)


class LarsenDelpetersonItem(scrapy.Item):
    LotNum = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
            delete_multiple_whitespaces,
            lambda x: x.split(' -- ')[0],
            lambda x: x.replace('Item # ', ''),
        ),
    )
    LotDescription = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
            delete_multiple_whitespaces,
        ),
    )
    City = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
        ),
    )
    State = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
            lambda x: x.split()[0]
        ),
    )
    ZIP = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
            lambda x: x.split()[-1]
        ),
    )
    Contact = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
        ),
    )
    Phone = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
        ),
    )
    Category = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
        ),
    )
    ClosesOn = scrapy.Field(
        input_processor=MapCompose(
            lambda x: x.strip(),
            delete_multiple_whitespaces,
        ),
    )
    image_urls = scrapy.Field(
        input_processor=MapCompose(
            absolute_url,
            clear_image_url
        ),
        output_processor=Identity()
    )
    images = scrapy.Field()
    folder_name = scrapy.Field()
