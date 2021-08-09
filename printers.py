import scrapy
from scrapy import Request
from ..items import PrintersonlineItem
import re
class PrintersSpider(scrapy.Spider):
    name = 'printers'
    allowed_domains = ['www.3dprintersonlinestore.com']
    start_urls = ['https://www.3dprintersonlinestore.com/index.php?route=product/search&search=printer']

    def parse(self, response):
        products = response.xpath("//div[@class='product product--zoom sold']")
        for product in products:
            link = product.xpath(".//div[@class='item active']/a/@href").get()
            yield response.follow(link, callback=self.parse_link)

        next_page = response.xpath("(//a[contains(text(), '>')])[1]/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
    def parse_link(self, response):
        items = PrintersonlineItem()
        items['title'] =  response.xpath("//div[@class='product-info__title']/h1/text()").get()
        items['price'] = response.xpath("//span[@class='price price-regular' or @class='price-box__new']/text()").get()
        items['Availability'] = response.xpath("(//div[@class='product-info__availability pull-right']//strong[@class='color']/text())[1]").get()
        items['Sold_by'] = response.xpath("//div[@class='product-info__description__brand']/a/@title").get()
        items['Warannty'] = response.xpath("//td[contains(text(), 'Manufacturer Warranty')]/following-sibling::td/text()").get()
        items['Layer_Thickness'] = response.xpath("//td[contains(text(), 'Layer Thickness')]/following-sibling::td/text()").get()
        items['Print_size'] = response.xpath("//td[contains(text(), 'Print size ( X Y Z )')]/following-sibling::td/text()").get()
        items['Print_Speed'] = response.xpath("//td[contains(text(), 'Print Speed')]/following-sibling::td/text()").get()
        items['Filament_Diameter'] = response.xpath("//td[contains(text(), 'Filament Diameter')]/following-sibling::td/text()").get()
        items['Nozzle_Diameter'] = response.xpath("//td[contains(text(), 'Nozzle Diameter')]/following-sibling::td/text()").get()
        items['Filament_Compatibility'] = response.xpath("//td[contains(text(), 'Filament Compatibility')]/following-sibling::td/text()").get()
        items['Print_Plate'] = response.xpath("//td[contains(text(), 'Print Plate (Build Platform)')]/following-sibling::td/text()").get()
        items['Printing_Software'] = response.xpath("//td[contains(text(), '3D Printing Software')]/following-sibling::td/text()").get()
        items['Supported_File_Formats'] = response.xpath("//td[contains(text(), 'Supported File Formats')]/following-sibling::td/text()").get()
        items['Operating_System'] = response.xpath("//td[contains(text(), 'Operating System')]/following-sibling::td/text()").get()
        items['AC_Input'] = response.xpath("//td[contains(text(), 'AC Input')]/following-sibling::td/text()").get()
        items['Power_Requirements'] = response.xpath("//td[contains(text(), 'Power Requirements')]/following-sibling::td/text()").get()
        if items['Power_Requirements'] is not None:
            items['Power_Requirements'] = re.sub(r'[\r\n]', '', items['Power_Requirements'])
        items['Connectivity_Interface'] = response.xpath("//td[contains(text(), 'Connectivity (Interface)')]/following-sibling::td/text()").get()
        items['Machine_weight'] = response.xpath("//td[contains(text(), 'Machine weight')]/following-sibling::td/text()").get()
        items['Machine_Dimensions'] = response.xpath("//td[contains(text(), 'Machine Dimensions')]/following-sibling::td/text()").get()

        yield items


