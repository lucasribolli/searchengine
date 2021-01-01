from backend.ES import ES
from elasticsearch_dsl import Document, Text

ES()

class Wikipedia(Document):
    url = Text()
    title = Text()
    lastmod = Text()
    text = Text()

    class Index:
        name = 'wikipedia'

    def save(self, **kwargs):
        return super(Wikipedia, self).save(kwargs)