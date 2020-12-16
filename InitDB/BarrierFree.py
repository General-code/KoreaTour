import requests
import json
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection.myproject
col = db.barrierFree

ServiceKey = 'yAXx8wVqlAhGVOpzwgRRwQxkxnafot%2FV6eRDkU7cJEEcY0X9K4XxkK9nONKC3Imu%2FSd0ZqgVfAufMLx9sdJMlA%3D%3D'
MobileApp = 'Test'
MobileOS = 'ETC'
pageNo = 1
numOfRows = 10
area_list = []
type = 'json'
contentId = 0

default_set = f"?ServiceKey={ServiceKey}&MobileApp={MobileApp}&MobileOS={MobileOS}&_type={type}"

# 키워드 조회에서 content type과 ID를 가져온다. 경도와 위도도 가져올 수 있다.
# 그것을 기반을
base_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorWithService/'
# not necessary
contentTypeCodes = {
    "관광지": 12,
    "문화시설": 14,
    "행사/공연/축제": 15,
    "여행코스": 25,
    "레포츠": 28,
    "숙박": 32,
    "쇼핑": 38,
    "음식점": 39,
}



# 1 지역코드 조회              x
# 2 서비스 분류코드 조회        x
# 3 지역기반 관광정보 조회      x
# 4 위치기반 관광정보 조회      ^
# 5 키워드 검색 조회           O
# 6 공통정보 조회(상세정보1)    O     공식홈페이지 주소를 얻을 수 있다.
# 7 소개정보 조회(상세정보2)    O
# 8 반복정보 조회(상세정보3)    O
# 9 이미지정보 조회(상세정보4)
# 10 무장애여행 조회(상세정보5) O

operations = [
    "areaCode",
    "categoryCode",
    "areaBasedList",
    "locationBasedList",
    "searchKeyword",
    "detailCommon",
    "detailIntro",
    "detailInfo",
    "detailImage",
    "detailWithTour",
]

# contentTypeId 와 contentId 의 casing이 매번 바뀐다.
# keyword 검색
keyword = '대구시 별 헤는 밤'
numOfRows = 100
pageNo = 1
res = requests.get(base_url + operations[4] + default_set + f'&numOfRows={numOfRows}&pageNo={pageNo}&keyword={keyword}')
data = res.json()
print(data)
data = data['response']['body']['items']['item']
addr = data['addr1'] + ' ' + data['addr2']
title = data['title']
contentid = data['contentid']
contenttypeid = data['contenttypeid']
coord = {'x':data['mapx'], 'y': data['mapy']}
print(contentid)

# 공통정보 조회 such as public sites to the tourist spot
res = requests.get(base_url + operations[5] + default_set + f'&contentId={contentid}')
print(res.text)


# 무장애 여행 API , 위도 경도 및 이미지 제공
barrier_free_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorWithService/' + operations[- 1]

# 1. 지역 코드 조회
# local_url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorWithService/areaCode' + f"?ServiceKey&_type={type}"

# 10. 무장애 여행 조회
# need contentId
# res = requests.get(
#     base_url +
#     f"?ServiceKey={ServiceKey}&MobileApp={MobileApp}&MobileOS={MobileOS}&pageNo={pageNo}&numOfRows={numOfRows}&_type=json&contentId={contentId}")
# xmlString = xml.text
# jsonString = json.dumps(xmltodict.parse(xmlString,encoding='UTF-8'),indent=4)
# data = json.loads(res.content)
# print(data['response']['body']['items']['item'])
# data = res['response']['body']['items']['item']
# print(data)


# for item in data:
#     print(item['name'])
#     area_list =
