# searchengine
Search engine using Scrapy Framework to get web data, Elasticsearch to store it, Flask to create APIs and JavaScript to search and visualizate it.

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
Please install 7.10.1 elasticsearch version and run it through `.bat` file
```
C:\elasticsearch-7.10.1\bin\elasticsearch.bat
```

## Run index_data.py
Be careful to not run twice.
```
cd ..\..
python index_data.py
```

