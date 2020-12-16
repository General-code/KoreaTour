from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
import requests

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


#  for Naver blog API

# For naver search service


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/show', methods=['GET'])
def show():
    title = request.args.get('title')
    search_keywords = request.args.get('searchKeyword')
    location = request.args.get('location')
    img_url = request.args.get('img_url')
    like = request.args.get('like')
    return render_template('show.html', title=title, search_keywords=search_keywords, location=location,
                           img_url=img_url, like=like)


@app.route('/show_blog', methods=['GET'])
def show_blogs():
    headers = {
        'X-Naver-Client-Id': '4DgH_eHrrKIpV5SkJxuL',
        'X-Naver-Client-Secret': 'WU9ri3ByPW',
    }

    params = {
        'query': '',
        'display': '3',
        'start': '1',
        'sort': 'sim',
    }
    params['query'] = request.args.get('title') + '맛집'
    response = requests.get('https://openapi.naver.com/v1/search/blog.json', headers=headers, params=params)
    data = response.json()
    print(data)
    return jsonify(data)


@app.route('/default', methods=['GET'])
def retreive_homepage_data():
    cursor = db.tourismAreaGallery
    data = list(cursor.find({}, {'_id': False, 'updatedDate': False}).sort('like', -1).limit(100))
    return jsonify(data)


@app.route('/search', methods=['GET'])
def search_keywords():
    # word = request.form['keyword']
    cursor = db.tourismAreaGallery
    data = list(cursor.find({}, {'_id': False}).sort('like', -1).limit(50))
    return jsonify(data)


@app.route('/hot50', methods=['GET'])
def hot_list():
    return True


# Yet to develope
# @app.route('/show',methods=['POST'])
# def show_page():
#     cursor = db.tourismAreaGallery
#     data = list(cursor.find({"searchKeyword"}, {'_id':False}),)
#     request.form['title']

# @app.route('/memo', methods=['GET'])
# def read_articles():
#     # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
#     memo_list = list(db.memo.find({},{'_id' : False}))
#     print(memo_list)
#     # 2. articles라는 키 값으로 articles 정보 보내주기
#     return jsonify({'result': 'success', 'articles': memo_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
