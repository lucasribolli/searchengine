from elasticsearch_dsl import Document, Text, Date, Keyword
from os.path import join
try:
    from backend.ES import ES
except ModuleNotFoundError:
    from ES import ES


ES()

class Wikipedia(Document):
    url = Text()
    title = Keyword()
    lastmod = Date()
    text = Keyword()
    accessdate = Date()

    class Index:
        name = 'wikipedia'

    def save(self, **kwargs):
        return super(Wikipedia, self).save(kwargs)