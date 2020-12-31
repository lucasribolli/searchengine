import scrapy
from wikipedia.items import Wikipedia
from bs4 import BeautifulSoup
import requests
import re

class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"

    def start_requests(self):
        # getting urls
        ROOT = "https://en.wikipedia.org"
        page = requests.get("https://en.wikipedia.org/wiki/List_of_programming_languages")
        soup = BeautifulSoup(page.text, 'html.parser')
        urls = []
        for ul in soup.find_all(class_='div-col'):
            for li in ul.find_all('ul'):
                for path in li.find_all('a'):
                    url = "{}{}".format(ROOT, path.get('href'))
                    urls.append(url)
        # crawling urls
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.xpath('//*[@id="footer-info-lastmod"]/text()').get():
            lastmod = response.xpath('//*[@id="footer-info-lastmod"]/text()').get().strip()
        if response.xpath("//*[@class='firstHeading']/i").get():
            title = response.xpath("//*[@class='firstHeading']/i/text()").get()
        elif response.xpath("//*[@class='firstHeading']/b").get():
            title = response.xpath("//*[@class='firstHeading']/b/text()").get()
        elif response.xpath("//*[@class='firstHeading']").get():
            title = response.xpath("//*[@class='firstHeading']/text()").get()
        page_content = response.xpath("//*[@id='mw-content-text']/div")
        paragraphs = []
        # only gets "p" values
        # lists, table, page with foreign languages
        # and another resources can be crawled in the future
        for paragraph in page_content.xpath('.//p'):
            if paragraph.xpath('string()').get():
                sentences = paragraph.xpath('string()').get() 
                sentences = sentences.replace('\n', '')
                sentences = re.sub(
                    pattern="[[]\d+[]]*", 
                    repl='', 
                    string=sentences)
                paragraphs.append(sentences)
        text = ' '.join(paragraphs)
        wikiarticle = Wikipedia(
            url = response.url,
            title = title if title else '',
            lastmod = lastmod if lastmod else '',
            text = text
        )
        yield wikiarticle