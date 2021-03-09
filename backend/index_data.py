from os.path import join
import pandas as pd
from uuid import uuid4
from ES import ES
from datetime import datetime
from Wikipedia import Wikipedia
from elasticsearch.exceptions import RequestError
from tqdm import tqdm
from elasticsearch.helpers import streaming_bulk


def _format_date(lastmod):
    date = lastmod.split("This page was last edited on")[-1].split(', at')[0].strip()
    time =  lastmod.split("This page was last edited on")[-1].split(', at')[-1].strip()
    datetime_str = '{} {}'.format(date, time)
    datetime_obj = datetime.strptime(datetime_str, '%d %B %Y %H:%M')
    return datetime_obj

def stream_doc(dataframe):
    for _, row in dataframe.iterrows():
        doc = {
            "_id": uuid4(),
            "url": row['url'] if 'url' in row else None,
            "title": row['title'] if 'title' in row else None,
            "lastmod": _format_date(row['lastmod']) if 'lastmod' in row else None,
            "text": row['text'] if 'text' in row else None,
            "accessdate": row['accessdate'] if 'accessdate' in row else datetime.now()
        }
        yield doc

def index():
    client = ES().get_client()
    index_name = Wikipedia().Index().name

    doc = pd.read_json(join("..","crawler","wikipedia","data","wikipedia.json"))
    number_of_docs = doc.shape[0]

    progress = tqdm(unit="docs", total=number_of_docs)
    successes = 0

    for ok, action in streaming_bulk(
        client=client, index=index_name, actions=stream_doc(doc),
    ):
        progress.update(1)
        successes += ok
    print(f"\nIndexed {successes}/{number_of_docs} documents", )


if __name__=="__main__":
    try:
        ES()
        index()
    except Exception as ex:
        print(ex)