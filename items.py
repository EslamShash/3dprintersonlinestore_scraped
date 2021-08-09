# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PrintersonlineItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    Availability = scrapy.Field()
    Sold_by = scrapy.Field()
    Warannty = scrapy.Field()
    Layer_Thickness = scrapy.Field()
    Print_size = scrapy.Field()
    Print_Speed = scrapy.Field()
    Filament_Diameter = scrapy.Field()
    Nozzle_Diameter = scrapy.Field()
    Filament_Compatibility = scrapy.Field()
    Print_Plate = scrapy.Field()
    Printing_Software = scrapy.Field()
    Supported_File_Formats = scrapy.Field()
    Operating_System = scrapy.Field()
    AC_Input = scrapy.Field()
    Power_Requirements = scrapy.Field()
    Connectivity_Interface = scrapy.Field()
    Machine_weight = scrapy.Field()
    Machine_Dimensions = scrapy.Field()

    pass
