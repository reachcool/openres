from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import chardet
import urllib2
from openres.items import Website

class ScholarSpider(Spider):
    name = "scholar"
    allowed_domains = ["glgoo.org"]
    def __init__(self, user=None):
    	self.start_urls = [
	    #"http://scholar.glgoo.org/citations?xpagesize=1000&user=%s" % user]
	    "http://scholar.glgoo.org/citations?view_op=search_authors&hl=en&mauthors=%s" % user]


    def parse(self,response):
	res = Selector(response)
	url = res.xpath('//h3/a/@href').extract()
	url_item = 'http://scholar.glgoo.org'+ str(url[0]) + '&pagesize=100'
	yield Request(url=url_item,callback=self.parse_all)

    def parse_all(self, response):
        sel = Selector(response)
        sites = sel.xpath('//tbody[@id="gsc_a_b"]/tr[@class="gsc_a_tr"]')

        cites = sel.xpath('//table[@id="gsc_rsb_st"]')
	
        items = []

#        for cite in cites:
        stat= Website()
        stat['total'] = cites.xpath('tr[2]/td[2]/text()').extract()
	  #  stat['total'] = cite.xpath('td[@class="gsc_a_t"]/a/text()').extract()
        stat['hindex'] = cites.xpath('tr[3]/td[2]/text()').extract()
	  #  stat['hindex'] = cite.xpath('td[@class="gsc_a_y"]/span[@class="gsc_a_h"]/text()').extract()
	stat['title'] = cites.xpath('tr[4]/td[2]/text()').extract()

	  #  print stat 
        items.append(stat)
#        return items
#
	for site in sites:
            item = Website()
            
            item['title'] = site.xpath('td[@class="gsc_a_t"]/a/text()').extract()
            item['authors'] = site.xpath('td[@class="gsc_a_t"]/div[@class="gs_gray"][1]/text()').extract()
	    item['source'] = site.xpath('td[@class="gsc_a_t"]/div[@class="gs_gray"][2]/text()').extract()
            item['year'] = site.xpath('td[@class="gsc_a_y"]/span[@class="gsc_a_h"]/text()').extract()
            item['citation'] = site.xpath('td[@class="gsc_a_c"]/a/text()').extract()
            items.append(item)
        
        return items

