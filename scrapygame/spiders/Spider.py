import csv
import pandas as pd
import scrapy

from scrapy.spiders import CrawlSpider
from ..parsers import parsers
from ..items import ScrapygameItem



class Spider(CrawlSpider):
    name = 'media'

    def __init__(self):

        # load urls from file
        df = pd.read_csv('scrapy_game_input.csv', index_col=False)
        self.urls = zip(df['id'].tolist(), df['url'].to_list())
        self.urls = [d for d in self.urls if '3dprintingindustry' in d[1]]

    def start_requests(self):
        for _id, url in self.urls:
            print(url)
            parser = self.get_parser(url)
            
            if parser is None:
                continue
            yield scrapy.Request(url, callback=lambda response : parser(response, _id))

    def get_parser(self, url):

        try:
            hostname = urlparse(url).netloc
            return parsers[hostname]
        except:
            pass
            return None
            
    # def parse_news(self, response):
    #     print(response.url)
        

    #     print('##### Parsing News #####')
    #     title = response.xpath("//article[@id='maincontent']//h1/text()").get()
    #     text = clear_text(response.xpath("//div[@class='articulum']/p//text()").getall())
    #     time = self.parse_time(response.xpath("//div[@class='nctimeshare']/time/@datetime").get().strip())
    #     # tag = ' '.join(response.xpath("//div[@class='article-hash-tag']/span/a/text()").getall())
    #     tag = ''

        
    #     return ScrapygameItem(_url=_url, title=title, author_name=author_name, contact_info=contact_info)




