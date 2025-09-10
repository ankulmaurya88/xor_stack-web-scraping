import scrapy

class W3SchoolsSpider(scrapy.Spider):
    name = 'w3schools'
    allowed_domains = ['w3schools.com']
    start_urls = ['https://www.w3schools.com/']

    def parse(self, response):
        # Extracting all links on the homepage
        links = response.css('a::attr(href)').getall()
        for link in links:
            yield {'link': link}
