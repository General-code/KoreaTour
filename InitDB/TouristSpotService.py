import requests
from pymongo import MongoClient

db = MongoClient('localhost', 27017)
col = db.TouristSpotService
doc = {}

base_url = 'http://api.visitkorea.or.kr/openapi/service?_type=json'
# Common Essential parameters
numOfRows = 100
pageNo = 0
MobileOS = 'ETC'
MobileApp = 'AppTest'
ServiceKey = 'yAXx8wVqlAhGVOpzwgRRwQxkxnafot%2FV6eRDkU7cJEEcY0X9K4XxkK9nONKC3Imu%2FSd0ZqgVfAufMLx9sdJMlA%3D%3D'



contentTypeIDCODES = {"관광지": 12,
               "문화시설": 14,
               "행사 공연 축제": 15,
               "여행코스": 25,
               "레포츠": 28,
               "숙박": 32,
               }

