# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import mysql.connector


class MoviescraperPipeline:

    def process_item(self, item, spider):
        duration_str = item.get('duration')

        if duration_str:
            hours_match = re.search(r'(\d+)h', duration_str)   #d+ match 1 ou plusieurs chiffres
            minutes_match = re.search(r'(\d+)m', duration_str)
            
            #convertir 'duration' films en minutes
            hours = int(hours_match.group(1)) if hours_match else 0
            minutes = int(minutes_match.group(1)) if minutes_match else 0

            total_minutes = hours * 60 + minutes
            item['duration'] = total_minutes 

        #transformer 'rating' en float
        rating_str = item.get('rating')
        if rating_str:
            item['rating']= float(rating_str)

        #transformer casting en chaine de caractéres
        casting_value = item.get('casting')
        if casting_value:
            item['casting'] = ", ".join(casting_value)



        return item




class SaveToMySqlPipeline:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'azertyuiop',
            database = 'films'
        )
        #create cursor to execute commands
        self.cursor = self.conn.cursor()

        #create movies table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies(
            id INT NOT NULL AUTO_INCREMENT,
            title TEXT,
            release_date INTEGER,
            rating DECIMAL,
            country VARCHAR(255),
            category VARCHAR(255),
            duration INTEGER,
            storyline VARCHAR(255),
            language VARCHAR(255),
            casting TEXT,
            PRIMARY KEY (id))

            """)


    def process_item(self, item, spider):
        self.cursor.execute(""" insert into movies (
            title,
            release_date,
            rating,
            country,
            category,
            duration,
            storyline,
            language,
            casting
            ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item["title"],
            item["release_date"],
            item["rating"],
            item["country"],
            item["category"],
            item["duration"],
            item["storyline"],
            item["language"],
            item["casting"]    
            ))
        
        self.conn.commit()
        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
