from pymongo import MongoClient


myclient = MongoClient('localhost',27017)
mydb = myclient['myproject']
mycol = mydb['tourismAreaGallery']


# HOT Place CARD SELECTING

# data = list(mycol.find({},{'_id':False,'searchKeyword':False}).sort('like',-1).limit(20))
# for i in data:
#     print(i)



