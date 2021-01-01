from backend.ES import ES
from backend.Wikipedia import Wikipedia


def test():
    wikipedia = Wikipedia()
    wikipedia.url = "https://127.0.0.1:8080/helloworld"
    wikipedia.title = "Hello, World!"
    wikipedia.lastmod = "1/1/2021"
    wikipedia.text = "Just testing."
    wikipedia.save()

if __name__=="__main__":
    ES()
    test()
    