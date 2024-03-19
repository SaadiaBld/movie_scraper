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


"""title = response.xpath('//h1[@data-testid]/span/text()').get()
        print("title:", title)
        release_date = response.xpath("//li[@data-testid= 'title-details-releasedate']//div//a/text()").get()
        print("date sortie:", release_date)
        rating = response.xpath('//div[@data-testid]/span/text()').get()
        country = response.xpath("//li[@data-testid= 'title-details-origin']//div//a/text()").get()
        print('pays:', country)
        category = response.xpath('//li[@data-testid="storyline-genres"]//li//text()').get()
        duration = response.xpath('//div//ul/li/text()').extract_first()
        storyline = response.xpath('//div[@data-testid="storyline-plot-summary"]//text()').get()
        language = response.xpath('//li[@data-testid="title-details-languages"]//a/text()').get()
        casting =response.xpath('//li[@data-testid="title-pc-principal-credit"]//a/text()').extract()[0:2]
        print('casting:', country)"""