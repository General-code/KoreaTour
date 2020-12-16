import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.myproject
col = db.weatherLocation

doc = {}
with open('../resources/Weather_location.csv', 'r') as f:
    rdr = csv.DictReader(f)
    for line in rdr:
        col.insert_one(line)

f.close()

