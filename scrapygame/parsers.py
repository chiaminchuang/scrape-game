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


    contact_info = response.xpath("//a[@class='SocialLink']/@href").get()
    if contact_info is not None and 'mailto' in contact_info:
        contact_info = contact_info.split(' ')[-1]
        return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)
    else:
        # redirect to author personal page
        def _info_parser(res):
            contact_info = res.xpath("//a[@class='SocialLink']/@href").get()
            contact_info = contact_info.split(' ')[-1] if 'mailto' in contact_info else contact_info

            return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

        return scrapy.Request(info_url, callback=_info_parser)

    
def _3dprintingindustry_parser(response):
    author_name = response.xpath("//div[@class='author-content']/h5/a/text()").get()
    contact_info = response.xpath("//div[@class='author-content']/a/@href").get()
    contact_info = decodeEmail(contact_info)
    
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

# -5
# redirect to the new home page
def _ambcrypto_parser(response):
    author_name = ''
    contact_info = ''
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _abccolumbia_parser(response):
    
    author_name = response.xpath("//div[@class='entry-meta entry-author multiple-bylines']/a/text()").get()
    contact_info = response.xpath("//div[@class='entry-meta entry-author multiple-bylines']/a/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)


def _altonivel_parser(response):
    author_name = response.xpath("//div[@class='writter']/a/text()").get()
    contact_info = response.xpath("//div[@class='writter']/a/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)


def _ainonline_parser(response):
    
    author_name = response.xpath("//div[@class='byline']/a/text()").get()
    contact_info = response.xpath("//div[@class='byline']/a/@href").get()
    contact_info = 'https://www.ainonline.com' + contact_info
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

# problem: need to login and subscribe 
# solution: download the whole page (html)
def _americanbanker_parser(response):

    author_name = response.xpath("//span[@class='ArticlePage-authorName']//a/text()").get()
    contact_info = response.xpath("//span[@class='ArticlePage-authorName']//a/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _androidworld_parser(response):

    author_name = response.xpath("//span[@class='autcont']/a/text()").get()
    contact_info = response.xpath("//a[@class='authsocial icon-instagram']/@href").get()

    if contact_info is None:
        contact_info = response.xpath("//span[@class='autcont']/a/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _3dnatives_parser(response):
    
    author_name = response.xpath("//div[@class='published-by']/strong/a/text()").get()
    contact_info = response.xpath("//div[@class='published-by']/strong/a/@href").get()

    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _alextimes_parser(response):
    
    author_name = response.xpath("//div[@class='td-post-author-name']/a/text()").get()
    contact_info = response.xpath("//div[@class='td-post-author-name']/a/@href").get()

    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _aerotelegraph_parser(response):
    

    author_name = response.xpath("//p[@class='post-meta clearfix']/a/text()").get().strip()
    info_url = response.xpath("//p[@class='post-meta clearfix']/a/@href").get()
    info_url = 'https://www.aerotelegraph.com' + info_url

    def _info_parser(res):
        # twitter
        contact_info = res.xpath("//a[@class='twitter_share']/@href").get()
        if contact_info is None:
            # email
            contact_info = res.xpath("//a[@class='email_share']/@href").get().split(':')[-1]

        return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

    return scrapy.Request(info_url, callback=_info_parser, dont_filter=True)
    
def _annistonstar_parser(response):

    author_name = response.xpath("//span[@class='tnt-byline asset-byline']/a[1]/text()").get()
    contact_info = response.xpath("//span[@class='tnt-byline asset-byline']/a[2]/@href").get()

    if author_name is None:
        author_name = response.xpath("//span[@class='tnt-byline']/text()").get()[3:]
    else:
        author_name = author_name.split(',')[0][3:]

    if contact_info is None:
        contact_info = response.xpath("//span[@class='tnt-byline asset-byline']/a[1]/@href").get()
        if contact_info is None:
            # no conact_info
            contact_info = ''
    else:
        contact_info = contact_info.split(':')[-1]

    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _anandtech_parser(response):

    author_name = response.xpath("//div[@class='blog_top_left']/span/a[2]/text()").get()
    contact_info = response.xpath("//div[@class='blog_top_left']/span/a[2]/@href").get()
    contact_info = 'https://www.anandtech.com' + contact_info

    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _androidpolice_parser(response):
    author_name = response.xpath("//a[@class='author-name']/text()").get()
    contact_info = response.xpath("//a[@class='author-name']/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _arstechnica_parser(response):
    
    author_name = response.xpath("//a[@class='author-name']/text()").get()
    
    # twitter
    contact_info = response.xpath("//section[@class='author-social']/a[2]/@href").get()
    if contact_info is None:
        # email
        contact_info = response.xpath("//section[@class='author-social']/a[1]/text()").get()

    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _androidcentral_parser(response):
    

    author_name = response.xpath("//span[@class='article-header__author']/a/text()").get()
    contact_info = response.xpath("//span[@class='article-header__author']/a/@href").get()
    contact_info = 'https://www.androidcentral.com' + contact_info
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)


def _247wallst_parser(response):
    
    author_name = response.xpath("//div[@class='author is-size-9 is-italic has-text-grey-darker has-text-weight-medium']/span/a/text()").get()
    contact_info = response.xpath("//div[@class='author is-size-9 is-italic has-text-grey-darker has-text-weight-medium']/span/a/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

# problem: need to login and subscribe 
# solution: download the whole page (html)
def _abqjournal_parser(response):
    author_name = response.xpath("//section[@class='entry-meta']//a/text()").get()
    contact_info = response.xpath("//section[@class='entry-meta']//a/@href").get()
    author_name = author_name.split('/')[0].strip()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)


def _aikenstandard_parser(response):

    text = response.xpath("//header[@class='asset-header']//span[@class='tnt-byline']/text()").get()

    if text is None:
        author_name = ''
        contact_info = ''
    else:
        text = text.replace('\n', ' ').split(' ')
        author_name = ' '.join(text[1:-1])
        contact_info = text[-1]
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)


# -4
# 403 error
def _agprofessional_parser(response):
    
    author_name = response.xpath("//a[@class='author-link']/text()").get()
    info_url = response.xpath("//a[@class='author-link']/href").get()
    info_url = 'https://www.agprofessional.com' + info_url

    def _info_parser(res):
        # twitter
        contact_info = res.xpath("//span[@class='contact-link email']/@href").get().split(':')[-1]
        if contact_info is None:
            # email
            contact_info = ''

        return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

    return scrapy.Request(info_url, callback=_info_parser, dont_filter=True)

def _303magazine_parser(response):

    author_name = response.xpath("//span[@class='cb-author']/a/text()").get()
    contact_info = response.xpath("//span[@class='cb-author']/a/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _almasdarnews_parser(response):
    
    author_name = response.xpath("//div[@class='td-post-author-name']/a/text()").get()
    contact_info = response.xpath("//div[@class='td-post-author-name']/a/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _americanthinker_parser(response):
    author_name = response.xpath("//div[@class='author']/a/text()").get()
    contact_info = response.xpath("//div[@class='author']/a/@href").get()
    contact_info = 'https://www.americanthinker.com' + contact_info
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _americanninjawarriornation_parser(response):

    author_name = response.xpath("//span[@class='c-byline__author-name']/text()").get()
    contact_info = response.xpath("//a[@class='c-byline__twitter-handle']/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _americanmilitarynews_parser(response):
    
    author_name = response.xpath("//a[@class='author url fn']/text()").get()
    contact_info = response.xpath("//a[@class='author url fn']/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

# -1
# redirect 301, no contact_info
def _africabusinesschief_parser(response):
    
    author_name = response.xpath("//div[@class='flex__SQ2u alignCenter__1AJm location__3QZp']/strong/text()").get()
    contact_info = ''
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _9and10news_parser(response):
    
    author_name = response.xpath("//div[@class='entry-meta entry-author multiple-bylines']/a/text()").get()
    contact_info = response.xpath("//div[@class='entry-meta entry-author multiple-bylines']/a/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _archpaper_parser(response):
    
    author_name = response.xpath("//a[@class='article--author']/text()").get()
    contact_info = response.xpath("//a[@class='article--author']/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _abovethelaw_parser(response):
    
    author_name = response.xpath("//p[@class='postAuthor byline']/a[@class='url fn']/text()").get()
    contact_info = response.xpath("//p[@class='postAuthor byline']/a[@class='url fn']/@href").get()
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)

def _architectsjournal_parser(response):

    author_name = response.xpath("//span[@class='post_author']//a[@class='author url fn']/text()").get()
    contact_info = response.xpath("//span[@class='post_author']//a[@class='author url fn']/@href").get()
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
  'ambcrypto.com': _ambcrypto_parser, 
  'www.abccolumbia.com': _abccolumbia_parser, 
  'www.altonivel.com.mx': _altonivel_parser, 
  'www.ainonline.com': _ainonline_parser, 
  'www.americanbanker.com': _americanbanker_parser, 
  'www.androidworld.it': _androidworld_parser, 
  'www.3dnatives.com': _3dnatives_parser, 
  'alextimes.com': _alextimes_parser, 
  'www.aerotelegraph.com': _aerotelegraph_parser, 
  'www.annistonstar.com': _annistonstar_parser, 
  'www.anandtech.com': _anandtech_parser, 
  'www.androidpolice.com': _androidpolice_parser, 
  'arstechnica.com': _arstechnica_parser, 
  'www.androidcentral.com': _androidcentral_parser, 
  '247wallst.com': _247wallst_parser, 
  'www.abqjournal.com': _abqjournal_parser, 
  'www.aikenstandard.com': _aikenstandard_parser, 
  'www.agprofessional.com': _agprofessional_parser, 
  '303magazine.com': _303magazine_parser, 
  'www.almasdarnews.com': _almasdarnews_parser, 
  'www.americanthinker.com': _americanthinker_parser, 
  'www.americanninjawarriornation.com': _americanninjawarriornation_parser, 
  'americanmilitarynews.com': _americanmilitarynews_parser, 
  'africa.businesschief.com': _africabusinesschief_parser, 
  'www.9and10news.com': _9and10news_parser, 
  'archpaper.com': _archpaper_parser, 
  'abovethelaw.com': _abovethelaw_parser, 
  'www.architectsjournal.co.uk': _architectsjournal_parser
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
