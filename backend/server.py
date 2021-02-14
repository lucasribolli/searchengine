"""
API searchengine
"""

from flask import Flask, jsonify, request, abort
from elasticsearch_dsl import Q
from elasticsearch.exceptions import ConnectionError
from flask_cors import CORS
from .Wikipedia import Wikipedia
from .ES import ES


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
ES()

RESULT_PER_PAGE = 3

"""
GET /api/search
data: List with elasticsearch dict hits
total: Int with total of hits
"""
@app.route('/api/search', methods=["GET"])
def search():
    try:
        search = request.args.get("q", type=str)
        page = request.args.get("page", type=int, default=0)
        start = page * RESULT_PER_PAGE
        end = start + RESULT_PER_PAGE

        wikipedia = Wikipedia()
        s = wikipedia.search()
        s = s.query("match", text=search)
        # s = s.sort('-lastmod')
        if s.count() > 0:
            data = []
            for hit in s[start:end]:
                data.append({
                "id": hit.meta.id,
                "url": hit.url if hasattr(hit, "url") else "",
                "title": hit.title if hasattr(hit, "title") else "",
                "lastmod": hit.lastmod if hasattr(hit, "lastmod") else "",
                "text": ' '.join(hit.text.split(' ')[:10]) if hasattr(hit, "text") else "",
                "accessdate": hit.accessdate if hasattr(hit, "accessdate") else "",
                })
            return jsonify({
                "data": data,
                "total": s.count(),
            })
        else:
            abort(404)
    except ConnectionError:
        abort(500)