import scrapy

class W3SchoolsSpider(scrapy.Spider):
    name = 'w3schools'
    allowed_domains = ['w3schools.com']
    start_urls = ['https://www.w3schools.com/']

    # def parse(self, response):
    #     # Extracting all links on the homepage
    #     links = response.css('a::attr(href)').getall()
    #     for link in links:
    #         yield {'link': link}

    def parse(self, response):
        # Extract page title
        title = response.css('title::text').get()

        # Extract headings
        h1_headings = response.css('h1::text').getall()
        h2_headings = response.css('h2::text').getall()
        h3_headings = response.css('h3::text').getall()

        # Extract paragraphs
        paragraphs = response.css('p::text').getall()

        # Extract links
        links = []
        for a in response.css('a'):
            text = a.css('::text').get()
            href = a.css('::attr(href)').get()
            if text and href:
                links.append({'text': text.strip(), 'href': href.strip()})

        yield {
            "title": title.strip() if title else "",
            "h1_headings": [h.strip() for h in h1_headings],
            "h2_headings": [h.strip() for h in h2_headings],
            "h3_headings": [h.strip() for h in h3_headings],
            "paragraphs": [p.strip() for p in paragraphs],
            "links": links
        }

