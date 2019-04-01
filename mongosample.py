import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["novicedataset"]

#make sure the names matches everywhere and it is case sensitive
mydict = { "name": "Dell XPS 13", "Price": 3000,
        "url":"https://amzon.in/kjdksd","category":"gaming","imgurl":"image url" }
x = mycol.insert_one(mydict)

mydict = { "name": "Dell XPS 15", "Price": 2000,
        "url":"https://amzon.in/kjddsd","category":"office","imgurl":"image url2" }
x = mycol.insert_one(mydict)
mydict = { "name": "hp XPS 16", "Price": 1000,
        "url":"https://amzon.in/kjddsd","category":"internet","imgurl":"image url2" }
x = mycol.insert_one(mydict)




mycol = mydb["cpu"]
#make sure the names matches everywhere and it is case sensitive
mydict = {
    "cpu" : "i5",
    "name" : "Intel i5 8 gen",
    "manufacturer" : "intel",
    "url" : "www.google.com/nn",
    "imgurl" : "www.google.com/nni",
    "price" : "2000"
}
x = mycol.insert_one(mydict)
mydict={
    "cpu" : "i5",
    "name" : "Intel i5 6 gen",
    "manufacturer" : "intel",
    "url" : "www.google.com/gg",
    "imgurl" : "www.google.com/ggi",
    "price" : "1000"
}
x = mycol.insert_one(mydict)
mydict={
    "cpu" : "i3",
    "name" : "Intel i3 6 gen",
    "manufacturer" : "intel",
    "url" : "www.google.com/gg",
    "imgurl" : "www.google.com/ggi",
    "price" : "10000"
}
x = mycol.insert_one(mydict)
mydict={
    "cpu" : "i3",
    "name" : "Intel i3 7 gen",
    "manufacturer" : "intel",
    "url" : "www.google.com/gg",
    "imgurl" : "www.google.com/ggi",
    "price" : "10090"
}

x = mycol.insert_one(mydict)
mycol = mydb["ram"]
mydict = {
    "ram" : "2",
    "name" : "Corsair 2GB",
    "manufacturer" : "Corsair",
    "url" : "www.google.com/gg",
    "imgurl" : "www.google.com/ggi",
    "price" : "1000"
}
x = mycol.insert_one(mydict)


mydict = {
    "ram" : "2",
    "name" : "Kingston 2GB",
    "manufacturer" : "Kingston",
    "url" : "www.google.com/ggf",
    "imgurl" : "www.google.com/fggi",
    "price" : "1300"
}
x = mycol.insert_one(mydict)

mydict ={
    "ram" : "4",
    "name" : "Corsair 4GB",
    "manufacturer" : "Corsair",
    "url" : "www.google.com/gg",
    "imgurl" : "www.google.com/ggi",
    "price" : "1000"
}
x = mycol.insert_one(mydict)

mydict ={
    "ram" : "4",
    "name" : "Kingston 4GB",
    "manufacturer" : "Kingston",
    "url" : "www.google.com/ggf",
    "imgurl" : "www.google.com/fggi",
    "price" : "1300"
}
x = mycol.insert_one(mydict)
