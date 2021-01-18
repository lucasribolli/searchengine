# searchengine
Search engine using Scrapy Framework to get web data, Elasticsearch to store it, Flask as backend and Vuejs Framework to search and visualizate it.

## Windows Setup

### Python environment
```
py -3 -m venv virtualenv
.\virtualenv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Run Scrapy
```
cd crawler\wikipedia
scrapy crawl wikipedia -O data\wikipedia.json
```

### Elasticsearch
In another terminal, install elasticsearch 7.10.1 and run it from `.bat` file.
For example:
```
C:\elasticsearch-7.10.1\bin\elasticsearch.bat
```

### Run index_data.py
Be careful to not run twice.
```
cd ..\..
python index_data.py
```

### Run Flask
```
cd backend
$env:FLASK_APP="server.py"
$env:FLASK_ENV="development"
flask run --host=0.0.0.0 --port=8088
```

