# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class MoviescraperPipeline:
    def process_item(self, item, spider):

        return item

class SaveToSqlitePipeline:

    def __init__(self):
        self.conn = sqlite3.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'films'
        )
        #create cursor to execute commands
        self.cursor = self.conn.cursor()

        #create movies table
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            id INT NOT NULL AUTO_INCREMENT,
            title TEXT,
            release_date INTEGER,
            rating DECIMAL,
            country VARCHAR(255),
            category VARCHAR(255),
            duration VARCHAR(255),
            storyline VARCHAR(255),
            language VARCHAR(255),
            casting TEXT
                         
            
            
                
                """)

        ))
