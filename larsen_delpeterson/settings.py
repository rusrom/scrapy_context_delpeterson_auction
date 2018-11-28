# -*- coding: utf-8 -*-

BOT_NAME = 'larsen_delpeterson'

SPIDER_MODULES = ['larsen_delpeterson.spiders']
NEWSPIDER_MODULE = 'larsen_delpeterson.spiders'

IMAGES_STORE = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'

ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_FIELDS = ['LotNum', 'LotDescription', 'City', 'State', 'ZIP', 'Contact', 'Phone', 'Category', 'ClosesOn']

ITEM_PIPELINES = {
    'larsen_delpeterson.pipelines.SalesPipeline': 300,
}
