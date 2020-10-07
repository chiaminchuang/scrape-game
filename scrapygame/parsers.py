from .items import ScrapygameItem
import scrapy

def decodeEmail(code):
    # e == /cdn-cgi/l/email-protection#85efe4e6eec5b6e1f5f7ecebf1ecebe2ecebe1f0f6f1f7fcabe6eae8
    code = code.split('#')[-1]
    decode = ''
    
    k = int(code[:2], 16)

    for i in range(2, len(code)-1, 2):
        decode += chr(int(code[i: i+2], 16)^k)

    return decode

def _applesfera_parser(response):
    author_name = response.xpath("//a[@class='article-author-link']/text()").get()
    contact_info = response.xpath("//a[@class='article-author-twitter']/@href").get()
    
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _ahoramismo_parser(response):
    author_name = response.xpath("//span[@class='c-meta__entity c-meta__entity--important vcard author fn']/a/text()").get()
    contact_info = response.xpath("//span[@class='c-meta__entity c-meta__entity--important vcard author fn']/a/@href").get()
    
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _africacgtn_parser(response):
    author_name = response.xpath("//div[@class='td-author-name vcard author']/span/a/text()").get()
    contact_info = response.xpath("//div[@class='td-author-name vcard author']/span/a/@href").get()
    
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _androidcommunity_parser(response):
    author_name = response.xpath("//div[@class='td-post-author-name']/a/text()").get()
    contact_info = response.xpath("//div[@class='td-post-author-name']/a/@href").get()

    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _analyticsindiamag_parser(response):
    author_name = response.xpath("//div[@class='author-content']/a/text()").get()
    contact_info = response.xpath("//div[@class='author-content']/a/@href").get()

    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _3dprintingmedia_parser(response):
    author_name = response.xpath("//h3[@class='author-name']/a/text()").get()
    contact_info = response.xpath("//div[@class='author-info']/li[@class='social-icons-item']/a/@href").get()
    if contact_info is None:
        contact_info = response.xpath("//h3[@class='author-name']/a/@href").get()

    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _accountingtoday_parser(response):
    

    author_name = response.xpath("//div[@class='ListiclePage-authorInfo-bio-name']/a/text()").get()
    info_url = response.xpath("//div[@class='ListiclePage-authorInfo-bio-name']/a/@href").get() 
    if author_name is None:
        author_name = response.xpath("//div[@class='ArticlePage-authorInfo-bio-name']/a/text()").get()
        info_url = response.xpath("//div[@class='ArticlePage-authorInfo-bio-name']/a/@href").get() 

    print(response.url)
    input()

    def _info_parser(res):
        contact_info = res.xpath("//a[@class='SocialLink']/@href").get()

        return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

    yield scrapy.Request(info_url, callback=_info_parser)

    

def _3dprintingindustry_parser(response):
    author_name = response.xpath("//div[@class='author-content']/h5/a/text()").get()
    contact_info = response.xpath("//div[@class='author-content']/a/@href").get()
    contact_info = decodeEmail(contact_info)
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)



parsers = {
  'www.applesfera.com': _applesfera_parser, 
  'ahoramismo.com': _ahoramismo_parser, 
  'africa.cgtn.com': _africacgtn_parser, 
  'androidcommunity.com': _androidcommunity_parser, 
  'www.analyticsindiamag.com': _analyticsindiamag_parser,
  'www.3dprintingmedia.network': _3dprintingmedia_parser, 
  'www.accountingtoday.com': _accountingtoday_parser, 
  '3dprintingindustry.com': _3dprintingindustry_parser, 
  'ambcrypto.com': 5, 
  'www.abccolumbia.com': 2, 
  'www.altonivel.com.mx': 3, 
  'www.ainonline.com': 6, 
  'www.americanbanker.com': 2, 
  'www.androidworld.it': 10, 
  'www.3dnatives.com': 11, 
  'alextimes.com': 6, 
  'www.aerotelegraph.com': 6, 
  'www.annistonstar.com': 7, 
  'www.anandtech.com': 8, 
  'www.androidpolice.com': 6, 
  'arstechnica.com': 6, 
  'www.androidcentral.com': 7, 
  '247wallst.com': 10, 
  'www.abqjournal.com': 4, 
  'www.aikenstandard.com': 5, 
  'www.agprofessional.com': 4, 
  '303magazine.com': 10, 
  'www.almasdarnews.com': 10, 
  'www.americanthinker.com': 1, 
  'www.americanninjawarriornation.com': 4, 
  'americanmilitarynews.com': 3, 
  'africa.businesschief.com': 1, 
  'www.9and10news.com': 2, 
  'archpaper.com': 3, 
  'abovethelaw.com': 1, 
  'www.architectsjournal.co.uk': 1
} 

# {
#   'www.applesfera.com': 2, 
#   'ahoramismo.com': 9, 
#   'africa.cgtn.com': 7, 
#   'androidcommunity.com': 9, 
#   'www.analyticsindiamag.com': 5,
#   'www.3dprintingmedia.network': 7, 
#   'www.accountingtoday.com': 5, 
#   '3dprintingindustry.com': 12, 
#   'ambcrypto.com': 5, 
#   'www.abccolumbia.com': 2, 
#   'www.altonivel.com.mx': 3, 
#   'www.ainonline.com': 6, 
#   'www.americanbanker.com': 2, 
#   'www.androidworld.it': 10, 
#   'www.3dnatives.com': 11, 
#   'alextimes.com': 6, 
#   'www.aerotelegraph.com': 6, 
#   'www.annistonstar.com': 7, 
#   'www.anandtech.com': 8, 
#   'www.androidpolice.com': 6, 
#   'arstechnica.com': 6, 
#   'www.androidcentral.com': 7, 
#   '247wallst.com': 10, 
#   'www.abqjournal.com': 4, 
#   'www.aikenstandard.com': 5, 
#   'www.agprofessional.com': 4, 
#   '303magazine.com': 10, 
#   'www.almasdarnews.com': 10, 
#   'www.americanthinker.com': 1, 
#   'www.americanninjawarriornation.com': 4, 
#   'americanmilitarynews.com': 3, 
#   'africa.businesschief.com': 1, 
#   'www.9and10news.com': 2, 
#   'archpaper.com': 3, 
#   'abovethelaw.com': 1, 
#   'www.architectsjournal.co.uk': 1
# } 
