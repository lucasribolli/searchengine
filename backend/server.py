from flask import Flask, jsonify, request
from backend import ES
from elasticsearch_dsl import Q, A
from backend import Wikipedia
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
ES()

@app.route('/api/search', methods=["GET"])
def search():
    search = request.json["search"]
    start = request.args.get("start", type=int, default=0)
    end = request.args.get("end", type=int, default=10)
    wikipedia = Wikipedia()
    s = wikipedia.search()
    q = Q("multi_match", 
            query=search, 
            fields=["title", "text"])
    s = s.query(q)
    #s = s.sort('-lastmod')
    data = []
    for hit in s[start:end]:
        data.append({
            "url": hit.url if hasattr(hit, "url") else "",
            "title": hit.title if hasattr(hit, "title") else "",
            "lastmod": hit.lastmod if hasattr(hit, "lastmod") else "",
            "text": hit.text if hasattr(hit, "text") else ""
        })
    return jsonify({
        "data": data,
        "total": s.count()
    })