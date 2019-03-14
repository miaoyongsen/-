# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WangzhanPipeline(object):
    def process_item(self, item, spider):

        with open('/Users/amiao/Desktop/zhongxinshengtai.txt','a') as fp:
            fp.write(item['name'])
        return item
