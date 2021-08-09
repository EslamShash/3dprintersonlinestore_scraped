# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class PrintersonlinePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('printers.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS printers""")
        self.curr.execute("""CREATE TABLE printers(
            title text,
            price text,
            Availability text,
            Sold_by text,
            Warannty text,
            Layer_Thickness text,
            Print_size text,
            Print_Speed text,
            Filament_Diameter text,
            Nozzle_Diameter text,
            Filament_Compatibility text,
            Print_Plate text,
            Printing_Software text,
            Supported_File_Formats text,
            Operating_System text,
            AC_Input text,
            Power_Requirements text,
            Connectivity_Interface text,
            Machine_weight text,
            Machine_Dimensions text
        )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO printers VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(
        item['title'],
        item['price'],
        item['Availability'],
        item['Sold_by'],
        item['Warannty'],
        item['Layer_Thickness'],
        item['Print_size'],
        item['Print_Speed'],
        item['Filament_Diameter'],
        item['Nozzle_Diameter'],
        item['Filament_Compatibility'],
        item['Print_Plate'],
        item['Printing_Software'],
        item['Supported_File_Formats'],
        item['Operating_System'],
        item['AC_Input'],
        item['Power_Requirements'],
        item['Connectivity_Interface'],
        item['Machine_weight'],
        item['Machine_Dimensions']

        ))
        self.conn.commit()
