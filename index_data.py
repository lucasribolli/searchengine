from backend.Wikipedia import Wikipedia
from datetime import datetime
from backend.ES import ES
import pandas as pd
import os

def format_date(lastmod):
    date = lastmod.split("This page was last edited on")[-1].split(', at')[0].strip()
    time =  lastmod.split("This page was last edited on")[-1].split(', at')[-1].strip()
    datetime_str = '{} {}'.format(date, time)
    datetime_obj = datetime.strptime(datetime_str, '%d %B %Y %H:%M')
    return datetime_obj

def index():
    wikipedia_data = pd.read_json(
        "crawler{0}wikipedia{0}data{0}wikipedia.json".format(os.path.sep))

    for _, row in wikipedia_data.iterrows():
        wikipedia = Wikipedia()
        wikipedia.url = row['url'] if 'url' in row else ''
        wikipedia.title = row['title'] if 'title' in row else ''
        wikipedia.lastmod = format_date(row['lastmod']) if 'lastmod' in row else None
        wikipedia.text = row['text'] if 'text' in row else ''
        wikipedia.save()

if __name__=="__main__":
    ES()
    index()
    