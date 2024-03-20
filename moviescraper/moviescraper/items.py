# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    release_date = scrapy.Field()
    rating = scrapy.Field()
    country = scrapy.Field()
    category = scrapy.Field()
    duration = scrapy.Field()
    storyline = scrapy.Field()
    language = scrapy.Field()
    casting = scrapy.Field()


