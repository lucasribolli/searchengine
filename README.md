# searchengine
Search engine using Scrapy Framework to get web data, Elasticsearch to store it, Flask as backend and Vuejs Framework to search and visualizate it.

## Python setup
```
py -3 -m venv virtualenv
.\virtualenv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run Scrapy
```
cd crawler\wikipedia
scrapy crawl wikipedia -O data\wikipedia.json
```

## Elasticsearch
In another terminal, install elasticsearch 7.10.1 and run it from `.bat` file.
For example:
```
C:\elasticsearch-7.10.1\bin\elasticsearch.bat
```

## Run index_data.py
Be careful to not run twice.
```
cd ..\..
python index_data.py
```

