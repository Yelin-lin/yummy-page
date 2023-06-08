from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.nv9rize.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/profile", methods=["POST"])
def profile_post():
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    hashtags_receive = request.form['hashtags_give']

    doc = {
        'url':url_receive,
        'name':name_receive,
        'comment': comment_receive,
        'hashtags': hashtags_receive
    }
    db.profile.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

@app.route("/profile", methods=["GET"])
def profile_get():
    all_profile = list(db.profile.find({},{'_id':False}))
    return jsonify({'result':all_profile})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)