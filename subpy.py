from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.ijt1e7j.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('subpage.html')

@app.route("/goodplace", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    star_receive = request.form['star_give']
    hashtags_receive = request.form['hatags_give']

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)
    
    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    oglocation = soup.select_one('meta[property="og:description"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']
    ogurl = soup.select_one('meta[property="og:url"]')['content']

    doc = {
        'title':ogtitle,
        'location':oglocation,
        'image':ogimage,
        'url': ogurl,
        'comment': comment_receive,
        'star':star_receive,
        'hashtags': hashtags_receive,
    }
    db.yummy.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

@app.route("/goodplace", methods=["GET"])
def movie_get():
    all_goodplace = list(db.yummy.find({},{'_id':False}))
    return jsonify({'result':all_goodplace})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)