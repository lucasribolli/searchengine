from scrapy.item import Item, Field


class Wikipedia(Item):
    url = Field()
    title = Field()
    lastmod = Field()
    text = Field()
    accessdate = Field()