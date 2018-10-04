# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BallerBasePipeline(object):
    def process_item(self, item, spider):
        return item

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class BallerImagesPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        # print ("plater \n\n\n")
        # print (item)
        return item



class BallerPlatePipeline(object):

    def process_item(self, item, spider):
        import baller.plater
        if not baller.plater.plater(item['image_paths']):
            raise DropItem("Images don't contain liscense plate")

        print ("<<<<<<<<<<<<<<<<<<<<<<<<<< \n\n\n")
        print ("baller found balls")
        
        return item
        # print ("Baller \n\n\n\n")
        # print (item['title'])
        # if item['price']:
        #     if item['price_excludes_vat']:
        #         item['price'] = item['price'] * self.vat_factor
        #     return item
        # else:
        #     raise DropItem("Missing price in %s" % item)