# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.settings.default_settings import BOT_NAME


class HhParsePipeline:
    def process_item(self, item, spider):
        return item


class HhMongoPipeline:
    def __init__(self):
        db_client = MongoClient()
        self.db = db_client[BOT_NAME]

    def process_item(self, item, spider):
        self.db[spider.name].insert_one(item)
        return item
