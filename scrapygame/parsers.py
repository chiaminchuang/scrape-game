

def _3dprintingindustry_parser(response, _id):
    author_name = response.xpath("//div[@class='author-content']//h5/text()").get()
    elements = response.xpath("//div[@class='author-content']//a").getall()
    contact_info = ''
    for ele in elements:
        if 'mailto:' in ele.attrib['href']:
          contact_info = ele.text.split(':')[-1]
          break

    return ScrapygameItem(_id=_id, url=response.url, author_name=author_name, contact_info=contact_info)



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
