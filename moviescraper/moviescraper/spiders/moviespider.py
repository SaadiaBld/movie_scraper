from scrapeme.items import MoviescraperItem
import scrapy


class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    '''custom_settings = {
        'FEEDS' : 'movie_data.json' : {'format': 'json', 'overwrite': True},
    }'''

    def parse(self, response): #definit l'element qui contient les films, pour indiquer l'url que spider suive le lien
        movies = response.xpath('//div[@data-testid="chart-layout-main-column"]/child::ul/li')

        for movie in movies:
            movie_url = movie.xpath('.//a/@href').get()
            yield response.follow(movie_url, self.parse_movie)


    def parse_movie(self,response):
        movie_item = MoviescraperItem()
        title = response.xpath('//h1[@data-testid]/span/text()').get()
        release_date = response.xpath("//li[@data-testid= 'title-details-releasedate']//div//a/text()").get()
        rating = response.xpath('//div[@data-testid]/span/text()').get()
        country = response.xpath("//li[@data-testid= 'title-details-origin']//div//a/text()").get()
        category = response.xpath('//li[@data-testid="storyline-genres"]//li//text()').get()
        duration = response.xpath('//div//ul/li/text()').extract_first()
        storyline = response.xpath('//div[@data-testid="storyline-plot-summary"]//text()').get()
        language = response.xpath('//li[@data-testid="title-details-languages"]//a/text()').get()
        casting =response.xpath('//li[@data-testid="title-pc-principal-credit"]//a/text()').extract()[0:2]