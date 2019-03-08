import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["novicedataset"]

mydict = { "name": "Dell XPS 13", "Price": 3000,
        "url":"https://amzon.in/kjdksd","category":"gaming","imgurl":"image url" }
x = mycol.insert_one(mydict)

mydict = { "name": "Dell XPS 15", "Price": 2000,
        "url":"https://amzon.in/kjddsd","category":"office","imgurl":"image url2" }
x = mycol.insert_one(mydict)
mydict = { "name": "hp XPS 16", "Price": 1000,
        "url":"https://amzon.in/kjddsd","category":"internet","imgurl":"image url2" }
x = mycol.insert_one(mydict)
