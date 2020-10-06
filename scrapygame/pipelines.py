# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
import csv

class ScrapygamePipeline:

    def __init__(self):
        self.filename = 'results.csv'
        # with open(self.filename , 'a', encoding='utf-8', newline='') as out:
        #     writer = csv.writer(out)
        #     writer.writerow(['id', 'url', 'author_name', 'contact_info'])

    def process_item(self, item, spider):
        print(item)
        with open(self.filename , 'a', encoding='utf-8', newline='') as out:
            writer = csv.writer(out)
            writer.writerow([item['_id'], item['url'], item['author_name'], item['contact_info']])

        return item
