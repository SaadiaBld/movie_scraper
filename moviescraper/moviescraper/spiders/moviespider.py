from moviescraper.items import MovieItem
import scrapy


class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    custom_settings = {
        'FEEDS' : {
            'filmdata.json' : {'format': 'json', 'overwrite': True},
        }
    }

# class CrawlerMovieSpider(CrawlSpider):
#     name = 'crawler_movies'
#     allowed_domains = ["www.imdb.com"]



    def parse(self, response): #definit l'element qui contient les films, pour indiquer l'url que spider suive le lien
        movies = response.xpath('//div[@data-testid="chart-layout-main-column"]/child::ul/li')

        for movie in movies:
            movie_url = movie.xpath('.//a/@href').get()
            yield response.follow(movie_url, self.parse_movie)


    def parse_movie(self,response):
        movie_item = MovieItem()
        #movie_item['url'] = response.url

        movie_item['title'] = response.xpath('//h1[@data-testid]/span/text()').get()
        movie_item['release_date'] = response.xpath('//h1[@data-testid="hero__pageTitle"]/following-sibling::*//a/text()').extract_first()
        movie_item['rating'] = response.xpath('//div[@data-testid]/span/text()').get()
        movie_item['country'] = response.xpath("//li[@data-testid= 'title-details-origin']//div//a/text()").get()

        print('pays:', movie_item['country'] )
        movie_item['category'] = response.xpath('//div[@data-testid="genres"]//a//text()').get()
        movie_item['duration'] = response.xpath('//div//ul/li/text()').extract_first()
        movie_item['storyline'] = response.xpath('//p[@data-testid="plot"]//text()').get()
        print('pays:', movie_item['storyline'] )

        movie_item['language'] = response.xpath('//li[@data-testid="title-details-languages"]//a/text()').get()
        movie_item['casting'] =response.xpath('//div[@data-testid = "title-cast-item"]//a/text()').getall()
        print('casting:',movie_item['casting'])

        yield movie_item


        {"title": "It Happened One Night", "release_date": "1934", "rating": "8.1", "country": "United States", "category": "Comedy", "duration": "1h 45m", "storyline": "A renegade reporter trailing a young runaway heiress for a big story joins her on a bus heading from Florida to New York, and they end up stuck with each other when the bus leaves them behin...", "language": "English", "casting": ["Clark Gable", "Claudette Colbert", "Walter Connolly", "Roscoe Karns", "Jameson Thomas", "Alan Hale", "Arthur Hoyt", "Blanche Friderici", "Charles C. Wilson", "Ernie Adams", "Jessie Arnold", "Irving Bacon", "William Bailey", "William Begg", "William A. Boardway", "Ward Bond", "Harry C. Bradley", "George P. Breakston"]}