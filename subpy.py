# import requests
# from bs4 import BeautifulSoup

# URL = 'https://place.map.kakao.com/814940188'
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(URL,headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')

# ogtitle = soup.select_one('meta[property="og:title"]')['content']
# oglocation = soup.select_one('meta[property="og:description"]')['content']
# ogimage = soup.select_one('meta[property="og:image"]')['content']
# ogurl = soup.select_one('meta[property="og:url"]')['content']

# print(ogtitle, oglocation, ogimage, ogurl)

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/goodplace", methods=["POST"])
def movie_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/goodplace", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)