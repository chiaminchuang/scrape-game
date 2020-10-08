import csv
import copy
import pandas as pd
import scrapy
from urllib.parse import urlparse

from scrapy.spiders import CrawlSpider
from ..parsers import parsers



class Spider(CrawlSpider):
    name = 'media'

    # handle_httpstatus_list = [301, 302]

    def __init__(self):

        # self.headers = {
        #     'Connection': 'keep-alive',
        #     'Cache-Control': 'max-age=0',
        #     'DNT': '1',
        #     'Upgrade-Insecure-Requests': '1',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        #     'Sec-Fetch-User': '?1',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        #     'Sec-Fetch-Site': 'same-origin',
        #     'Sec-Fetch-Mode': 'navigate',
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Accept-Language': 'en-US,en;q=0.9',
        # }

        # load urls from file
        df = pd.read_csv('scrapy_game_input.csv', index_col=False)
        self.urls = zip(df['id'].tolist(), df['url'].to_list())
        # self.urls = [d for d in self.urls if 'architectsjournal' in d[1]]

        with open('results.csv' , 'w', encoding='utf-8', newline='') as out:
            writer = csv.writer(out)
            writer.writerow(['id', 'url', 'author_name', 'contact_info'])


    def start_requests(self):
        for _id, url in self.urls:
            # print(_id, url)
            parser = self.get_parser(url)
            
            if parser is None:
                continue
            yield scrapy.Request(url, callback=parser, meta={'_id': _id}, dont_filter=True)

    def get_parser(self, url):

        try:
            hostname = urlparse(url).netloc
            return parsers[hostname]
        except Exception as e:
            print(e)
            
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




