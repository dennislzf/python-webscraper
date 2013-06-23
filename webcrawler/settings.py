# Scrapy settings for webcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'webcrawler'
BOT_VERSION = '1.0'
ITEM_PIPELINES = [
    'webcrawler.pipelines.ElectronicsSQLPipeline','webcrawler.pipelines.ClothingPipeline'
]
SPIDER_MODULES = ['webcrawler.spiders']
NEWSPIDER_MODULE = 'webcrawler.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

