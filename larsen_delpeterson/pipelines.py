# -*- coding: utf-8 -*-

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re


class LarsenDelpetersonPipeline(object):
    def process_item(self, item, spider):
        return item


class SalesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return [Request(x, meta={'image_name': item['LotNum'], 'folder_name': item['folder_name'], 'n': img_index}) for img_index, x in enumerate(item.get('image_urls', []), 1)]

    def file_path(self, request, response=None, info=None):
        return 'delpeterson/{folder_name}/{img_name}_{img_index}.jpg'.format(
            folder_name=request.meta['folder_name'],
            img_name=request.meta['image_name'],
            img_index=request.meta['n']
        )
