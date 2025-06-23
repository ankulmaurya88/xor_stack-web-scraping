import scrapy
import json


class PythonQuestionsSpider(scrapy.Spider):
    name = "python_questions"
    allowed_domains = ["api.stackexchange.com"]
    start_urls = [
        "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&tagged=python&site=stackoverflow"
    ]

    def parse(self, response):
        data = json.loads(response.text)
        for i, item in enumerate(data.get("items", [])[:10], 1):
            yield {
                "title": item["title"],
                # "link": item["link"]
            }
