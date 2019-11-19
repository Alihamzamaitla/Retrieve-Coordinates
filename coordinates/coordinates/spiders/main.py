# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from collections import OrderedDict
class MainSpider(Spider):
    name = 'main'
    allowed_domains = ['portalinmobiliario.com']
    start_urls = ['https://portalinmobiliario.com/arriendo/departamento/parque-bicentenario-vitacura-santiago-metropolitana']    
    def parse(self, response):
        for Link in response.xpath('//*[@class="item__info-link"]/@href').extract():
            yield (Request(Link,callback=self.parse2))
        Next_url =response.xpath('//*[@class="andes-pagination__link prefetch"]/@href').extract_first()
        yield Request(Next_url,callback=self.parse)
    def parse2(self,response):
        Mydata = OrderedDict()
        Link=response.url
        Type="".join(response.xpath('//*[@class="vip-classified-info"]/dl/text()').extract()).replace("\t", "").replace("\n","")
        Apartment=response.xpath('//*[@class="map-address"]/text()').extract_first()
        Search_Criteria=''.join(response.xpath('//*[@class="vip-navigation-breadcrumb-list"]/li/a//text()').extract()).replace("\t", "").replace("\n"," ")
        Price=response.xpath('//*[@class="price-tag-symbol"][contains(text(),"$")]/@content').extract_first()
        Publish_date=response.xpath('//*[@class="official-store-info info-property-date"]/p[2]/text()').extract_first()
        Total_area=response.xpath('//*[@class="specs-item"]/strong[contains(text(),"Superficie total")]/parent::*/span/text()').extract_first()
        Efective_area=response.xpath('//*[@class="specs-item"]/strong[contains(text(),"Superficie útil")]/parent::*/span/text()').extract_first()
        Bedrooms=response.xpath('//*[@class="specs-item"]/strong[contains(text(),"Dormitorios")]/parent::*/span/text()').extract_first()
        Baths=response.xpath('//*[@class="specs-item"]/strong[contains(text(),"Baños")]/parent::*/span/text()').extract_first()
        Description="".join(response.xpath('//*[@class="item-description__text"]/p/text()').extract())
        Coordinates=response.xpath('/html/body/script[4]/text()').extract_first().split("latitude: ")[1][0:11].replace(",","")  +","+ response.xpath('/html/body/script[4]/text()').extract_first().split("longitude: ")[1][0:11].replace(",","")   

        Mydata['Link'] =Link
        Mydata['Type'] =Type
        Mydata['Search_Criteria'] =Search_Criteria
        Mydata['Apartment'] = Apartment     
        Mydata['Price'] =Price
        Mydata['Publish_date'] =Publish_date
        Mydata['Total_area'] =Total_area
        Mydata['Efective_area'] =Efective_area
        Mydata['Bedrooms'] =Bedrooms
        Mydata['Baths'] =Baths
        Mydata['Description'] =Description
        Mydata['Coordinates'] =Coordinates
        yield Mydata


        # l.add_value("Link",Link)
        # l.add_value("Type",Type)
        # l.add_value("Search_Criteria",Search_Criteria)
        # l.add_value("Apartment",Apartment)
        # l.add_value("Price",Price)
        # l.add_value("Publish_date",Publish_date)
        # l.add_value("Total_area",Total_area)
        # l.add_value("Efective_area",Efective_area)
        # l.add_value("Bedrooms",Bedrooms)
        # l.add_value("Baths",Baths)
        # l.add_value("Description",Description)
        # l.add_value("Coordinates",Coordinates)

        # yield l.load_item()