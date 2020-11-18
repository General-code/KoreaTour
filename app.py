from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/default', methods=['GET'])
def retreive_homepage_data():
    cursor = db.tourismAreaGallery
    data = list(cursor.find({},{'_id':False,'searchKeyword':False,'updatedDate':False}).sort('like',-1).limit(8))
    for i in range(0,8):
        print(data[i])
    return jsonify(data)

# @app.route('/memo', methods=['GET'])
# def read_articles():
#     # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
#     memo_list = list(db.memo.find({},{'_id' : False}))
#     print(memo_list)
#     # 2. articles라는 키 값으로 articles 정보 보내주기
#     return jsonify({'result': 'success', 'articles': memo_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
