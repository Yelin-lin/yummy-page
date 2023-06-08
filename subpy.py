import certifi
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


ca = certifi.where()

client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.ijt1e7j.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


import requests
from bs4 import BeautifulSoup

# 태준 route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/yelin')
def subpage():
    return render_template('subpage.html')

@app.route('/taejun')
def taejun():
    return render_template('taejun.html')

@app.route('/rec')
def rec_html():
    return render_template('rec.html')

@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.fan.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comment = list(db.fan.find({}, {'_id': False}))
    return jsonify({'result': all_comment})

# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5001, debug=True)

#예린 route


@app.route("/goodplace", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    star_receive = request.form['star_give']
    hashtags_receive = request.form['hashtags_give']
    imgurl_receive = request.form['imgurl_give']

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    
    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    oglocation = soup.select_one('meta[property="og:description"]')['content']
    ogurl = soup.select_one('meta[property="og:url"]')['content']

    doc = {
        'title':ogtitle,
        'location':oglocation,
        'image':imgurl_receive,
        'url': ogurl,
        'comment': comment_receive,
        'star':star_receive,
        'hashtags': hashtags_receive,
    }
    db.yummy.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

@app.route("/taejunplace", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    star_receive = request.form['star_give']
    hashtags_receive = request.form['hashtags_give']
    imgurl_receive = request.form['imgurl_give']

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    
    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    oglocation = soup.select_one('meta[property="og:description"]')['content']
    ogurl = soup.select_one('meta[property="og:url"]')['content']

    doc = {
        'title':ogtitle,
        'location':oglocation,
        'image':imgurl_receive,
        'url': ogurl,
        'comment': comment_receive,
        'star':star_receive,
        'hashtags': hashtags_receive,
    }
    db.taejun.insert_one(doc)

    return jsonify({'msg':'저장완료!'})



@app.route("/goodplace", methods=["GET"])
def movie_get():
    all_goodplace = list(db.yummy.find({},{'_id':False}))
    return jsonify({'result':all_goodplace})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)