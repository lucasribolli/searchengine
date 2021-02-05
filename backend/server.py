"""
API searchengine
"""

from flask import Flask, jsonify, request, abort
from elasticsearch_dsl import Q
from flask_cors import CORS
from . import Wikipedia
from . import ES


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
ES()

RESULT_PER_PAGE = 3

"""
GET /api/search
data: List with elasticsearch hits
total: Int with total of hits
"""
@app.route('/api/search', methods=["GET"])
def search():
    search = request.args.get("q", type=str)
    page = request.args.get("page", type=int, default=0)
    start = page * RESULT_PER_PAGE
    end = start + RESULT_PER_PAGE

    wikipedia = Wikipedia()
    s = wikipedia.search()
    s = s.query("match", text=search)
    s = s.sort('-lastmod')
    data = []
    for hit in s[start:end]:
        data.append({
          "id": hit.meta.id,
          "url": hit.url if hasattr(hit, "url") else "",
          "title": hit.title if hasattr(hit, "title") else "",
          "lastmod": hit.lastmod if hasattr(hit, "lastmod") else "",
          "text": hit.text if hasattr(hit, "text") else "",
          "accessdate": hit.accessdate if hasattr(hit, "accessdate") else "",
        })
    if s.count() > 0:
        return jsonify({
            "data": data,
            "total": s.count(),
        })
    abort(404)