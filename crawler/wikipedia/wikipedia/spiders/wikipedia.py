import scrapy
from wikipedia.items import Wikipedia
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"

    """
    Getting urls in two different pages
    """
    @staticmethod
    def _urls():
        ROOT = "https://en.wikipedia.org"
        page_urls = {
            "prog_lang": f"{ ROOT }/wiki/List_of_programming_languages",
            "philop": f"{ ROOT }/wiki/List_of_philosophies"
        }
        urls = []
        for main_name, main_url in page_urls.items():
            page = requests.get(main_url)
            soup = BeautifulSoup(page.text, 'html.parser')
            if main_name == "prog_lang":
                for ul in soup.find_all(class_='div-col'):
                    for li in ul.find_all('ul'):
                        for path in li.find_all('a'):
                            url = f"{ ROOT }{ path.get('href') }"
                            urls.append(url)
            elif main_name == "philop":
                for p in soup.find_all('p'):
                    for a in p:
                        try:
                            if a.get('href') is None:
                                continue
                            url = f"{ ROOT }{ a.get('href') }"
                            urls.append(url)
                        except:
                            pass
        return urls

    def start_requests(self):
        urls = WikipediaSpider()._urls()
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
        text = ' '.join(paragraphs[:10])
        wikiarticle = Wikipedia(
            url = response.url if response.url else None,
            title = title if title else None,
            lastmod = lastmod if lastmod else None,
            text = text if text else None,
            accessdate = datetime.now()
        )
        yield wikiarticle