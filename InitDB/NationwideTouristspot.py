from pymongo import MongoClient
import requests
import json

db = MongoClient('localhost', 27017)
db = db.myproject
col = db.nationwideTourismspot


base_url = 'http://api.data.go.kr/openapi/tn_pubr_public_trrsrt_api'
type = 'json'
numOfRows = 100
pageNo = 0
ServiceKey = 'yAXx8wVqlAhGVOpzwgRRwQxkxnafot%2FV6eRDkU7cJEEcY0X9K4XxkK9nONKC3Imu%2FSd0ZqgVfAufMLx9sdJMlA%3D%3D'
res = requests.get(base_url + f'?ServiceKey={ServiceKey}&type={type}&numOfRows={numOfRows}&pageNo={pageNo}' )
