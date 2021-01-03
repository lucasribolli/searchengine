# searchengine
Search engine using Scrapy Framework to get web data, Elasticsearch to store it, Flask to create APIs and JavaScript to search and visualizate it.

## Run Scrapy
```
cd crawler/wikipedia
```
```
scrapy crawl wikipedia -O data\wikipedia.json
```

## Run index_data.py
Be careful to not run twice.
```
cd ..
```
```
cd ..
```
```
python index_data.py
```
