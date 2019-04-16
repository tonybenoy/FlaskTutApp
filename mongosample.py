import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["novicedataset"]

#make sure the names matches everywhere and it is case sensitive
mydict = {
    "name" : "Dell XPS 13",
    "Price" : 3000,
    "url" : "https://amzon.in/kjdksd",
    "category" : "gaming",
    "manufacturer" : "Dell",
    "imgurl" : "image url",
    "ram" : "4 GB",
    "cpu" : "i5",
    "hdd" : "1TB",
    "gpu" : "2 GB"
}
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

mycol = mydb["gpu"]
mydict = {
    "GPU" : "4 GB",
    "name" : "AMD m2 4GB",
    "manufacturer" : "AMD",
    "url" : "www.google.com/gg",
    "imgurl" : "www.google.com/ggi",
    "price" : "2000"
}

x = mycol.insert_one(mydict)
mycol = mydb["hdd"]
mydict = {
    "hdd" : "1 TB",
    "name" : "Corsair TB",
    "manufacturer" : "Corsair",
    "url" : "www.google.com/gg",
    "imgurl" : "www.google.com/ggi",
    "price" : "1000"
}
x = mycol.insert_one(mydict)

mycol = mydb["motherboard"]
mydict = {
    "mb" : "AM4 Socket Type",
    "name" : "AM4 Socket Type sdkdn",
    "manufacturer" : "AM4",
    "url" : "www.google.com/nn",
    "imgurl" : "www.google.com/nni",
    "price" : "2000"
}
x = mycol.insert_one(mydict)

mycol = mydb["powersupply"]
mydict = {
    "powersupply" : "4 Watt",
    "name" : "Nvdia 4 WATT",
    "manufacturer" : "Nvdia",
    "url" : "www.google.com/gg",
    "imgurl" : "www.google.com/ggi",
    "price" : "3000"
}
x = mycol.insert_one(mydict)

