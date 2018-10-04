import scrapy
from scrapy import Request
from baller.items import BallerItem

class TestSpider(scrapy.Spider):
    name = "TestSpider"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://houston.craigslist.org/search/cto?sort=date&hasPic=1&max_price=10000"]


    def parse(self, response):
        absolute_url = "https://houston.craigslist.org/cto/d/2000-dogde-stratus/6703101157.html"
        
        yield Request(absolute_url, callback=self.parse_page, meta={'URL': absolute_url, 'Title': "Test", 'Address':"Home" })

            
    def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        address = response.meta.get('Address')
        
        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract()).strip()
        
        attrs = response.xpath('//p[@class="attrgroup"]//span//text()').extract()
        attrs_dic = {
            'model' : attrs[0]
            , 'condition': 'n/a'
            , 'cylinders' : 'n/a'
            , 'drive' : 'n/a'
            , 'fuel' : 'n/a'
            , 'odometer' : 'n/a'
            , 'paint color' : 'n/a'
            , 'size' : 'n/a'
            , 'title status' : 'n/a'
            , 'transmission' : 'n/a'
            , 'type' : 'n/a'
        }
        for i in range(0, len(attrs)):
            if attrs[i].split(":")[0] in attrs_dic and i + 1 < len(attrs):
                attrs_dic[attrs[i]] = str(attrs[i+1])

        image_urls = []
        imgs = response.xpath('//a[@class="thumb"]')
        for img in imgs:
            imglink = img.xpath('@href').extract_first()
            imglink = imglink.replace("600x450", "1200x900")
            image_urls.append(imglink)
            # imgtitle = title[:6] + ige.xpath('@title').extract_first()
            
        yield BallerItem(
            url = url
            , title = title
            , address = address
            , detail = attrs_dic
            , image_urls = image_urls
        )