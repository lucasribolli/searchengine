from flask import Flask, jsonify, request
from ES import ES
from Wikipedia import Wikipedia

app = Flask(__name__)
ES()

@app.route('/getalltext', methods=["GET"])
def getalltext():
    wikipedia = Wikipedia()
    s = wikipedia.search()
    s = s.query("match_all")
    data = []
    for hit in s:
        data.append({
            "url": hit.url,
            "title": hit.title,
            "lastmod": hit.lastmod,
            "text": hit.text
        })
    return jsonify({
        "data": data,
        "total": s.count()
    })

@app.route('/getbytitle', methods=["GET"])
def get_by_title():
    title = request.args.get("title", 
                            type=str,
                            default="Python")
    wikipedia = Wikipedia()
    s = wikipedia.search()
    s = s.query("match", title=title)
    data = []
    for hit in s:
        data.append({
            "url": hit.url,
            "title": hit.title,
            "lastmod": hit.lastmod,
            "text": hit.text
        })
    return jsonify({
        "data": data,
        "total": s.count()
    })