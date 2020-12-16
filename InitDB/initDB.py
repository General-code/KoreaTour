from pymongo import MongoClient
import requests
import json

# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.myproject
service_key = 'yAXx8wVqlAhGVOpzwgRRwQxkxnafot%2FV6eRDkU7cJEEcY0X9K4XxkK9nONKC3Imu%2FSd0ZqgVfAufMLx9sdJMlA%3D%3D'
numOfRows = 10
# db.tourismAreaGallery.drop()

for i in range(1,3):

    pageNo = i
    base_url = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList?ServiceKey={}&numOfRows={}&pageNo={}&MobileOS=ETC&MobileApp=TestApp&_type=json'.format(
        service_key, numOfRows, pageNo)

    #  id, updatedDate ,Data keyword, img_url, 지역이름, 관광지 이름, galViewCount를 Like로 받는다. 를 이용한 검색 mongoDB
    res = requests.get(base_url)
    if res.text.strip() != '':

        tourism_jsondata = json.loads(res.text)
        data_rows = tourism_jsondata['response']['body']['items']['item']
    else:
        break


    for row in data_rows:
        print(row)
        # if not row.get('galSearchKeyword'):
        #     searchKeyword=''
        # else:
        #     searchKeyword = row['galSearchKeyword']
        #
        # if row.get('galPhotographyLocation'):
        #     location = row['galPhotographyLocation']
        #
        # updatedDate = row['galModifiedtime']
        # title = row['galTitle']
        # like = row['galViewCount']
        # img_url = row['galWebImageUrl']
        #
        # print(location)
        # print(searchKeyword)
        # print(title)
        # print(like)
        # print(img_url)
        #
        # if '종교' not in searchKeyword:
        #     doc = {"updatedDate": updatedDate, 'location': location, 'searchKeyword': searchKeyword, "title": title,
        #            'like': like, 'img_url': img_url}
        #     db.tourismAreaGallery.insert_one(doc)
