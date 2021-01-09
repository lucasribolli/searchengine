from elasticsearch_dsl import Document, Text, Date
from . import ES


ES()

class Wikipedia(Document):
    url = Text()
    title = Text()
    lastmod = Date()
    text = Text()

    class Index:
        name = 'wikipedia'

    def save(self, **kwargs):
        return super(Wikipedia, self).save(kwargs)