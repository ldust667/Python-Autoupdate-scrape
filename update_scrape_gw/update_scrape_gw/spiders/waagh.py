import scrapy

#creating class implementation of a scrapy.Spider object
class WaaghSpider(scrapy.Spider):
	name='waagh'
	start_urls = ['https://www.games-workshop.com']
	
	def parse(self,response):
        	urls = [
            		'https://www.games-workshop.com/en-US/Orks-Warboss-Grukks-Boss-Mob-2018'
        	]
        	for url in urls:
            		yield scrapy.Request(url=url, callback=self.parse)

    	def parse(self, response):
        	page = response.url.split("/")[-2]
        	filename = 'quotes-%s.html' % page
        	with open(filename, 'wb') as f:
            		f.write(response.body)
        	self.log('Saved file %s' % filename)













'''
		#proceed to the other links on the page
		for page_url in response.css('a[title ~= page]').extract():
            		page_url = response.urljoin(page_url)
            		yield scrapy.Request(url=page_url, callback=self.parse)


	# extract the torrent items
        	for tr in response.css('table.lista2t tr.lista2'):
            		tds = tr.css('td')
            		link = tds[1].css('a')[0]
            		yield {
                		'title' : link.css('::attr(title)').extract_first(),
                		'url' : response.urljoin(link.css('::attr(href)').extract_first()),
                		'date' : tds[2].css('::text').extract_first(),
                		'size' : tds[3].css('::text').extract_first(),
                		'seeders': int(tds[4].css('::text').extract_first()),
                		'leechers': int(tds[5].css('::text').extract_first()),
                		'uploader': tds[7].css('::text').extract_first(),
            }
'''
