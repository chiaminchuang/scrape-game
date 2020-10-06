from .items import ScrapygameItem

def decodeEmail(code):
    # e == /cdn-cgi/l/email-protection#85efe4e6eec5b6e1f5f7ecebf1ecebe2ecebe1f0f6f1f7fcabe6eae8
    code = code.split('#')[-1]
    decode = ''
    
    k = int(code[:2], 16)

    for i in range(2, len(code)-1, 2):
        decode += chr(int(code[i: i+2], 16)^k)

    return decode


def _3dprintingindustry_parser(response):
    author_name = response.xpath("//div[@class='author-content']/h5/a/text()").get()
    contact_info = response.xpath("//div[@class='author-content']/a/@href").get()
    contact_info = decodeEmail(contact_info)
    # contact_info = ''
    # for ele in elements:
        
    #     text = ele.xpath('@href').get()
    #     print(text)
    #     input()

    #     if 'mailto:' in text:
    #         contact_info = text.split(':')[-1]
    #         break
        
    # print(_id, response.url, author_name, contact_info)
    return ScrapygameItem(_id=response.meta.get('_id'), url=response.url, author_name=author_name, contact_info=contact_info)



parsers = {
  'www.applesfera.com': 2, 
  'ahoramismo.com': 9, 
  'africa.cgtn.com': 7, 
  'androidcommunity.com': 9, 
  'www.analyticsindiamag.com': 5,
  'www.3dprintingmedia.network': 7, 
  'www.accountingtoday.com': 5, 
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
