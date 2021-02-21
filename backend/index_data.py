from os.path import join
import pandas as pd
from uuid import uuid4
from datetime import datetime
from Wikipedia import Wikipedia
from ES import ES


def _format_date(lastmod):
    date = lastmod.split("This page was last edited on")[-1].split(', at')[0].strip()
    time =  lastmod.split("This page was last edited on")[-1].split(', at')[-1].strip()
    datetime_str = '{} {}'.format(date, time)
    datetime_obj = datetime.strptime(datetime_str, '%d %B %Y %H:%M')
    return datetime_obj

def index():
    wikipedia_data = pd.read_json(join("..","crawler","wikipedia","data","wikipedia.json"))

    for i, row in wikipedia_data.iterrows():
        wikipedia = Wikipedia(id=uuid4())
        wikipedia.url = row['url'] if 'url' in row else ''
        wikipedia.title = row['title'] if 'title' in row else ''
        wikipedia.lastmod = _format_date(row['lastmod']) if 'lastmod' in row else None
        wikipedia.text = row['text'] if 'text' in row else ''
        wikipedia.accessdate = row['accessdate'] if 'accessdate' in row else datetime.now()
        wikipedia.save()
    
    ## return with plus 1 because iterrows function starts with key 0
    return i + 1

if __name__=="__main__":
    try:
        ES()
        Wikipedia().init()
        print("Indexing...", end="\r")
        indexed = index()
        print(f"Indexed {indexed} content(s) successfully!")
    except Exception as ex:
        print(ex)