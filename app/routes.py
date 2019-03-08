from app import app
from flask import render_template
from app.forms import NoviceForm
import pymongo
@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    form = NoviceForm() 
    if form.validate_on_submit():
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["novicedataset"]
        if form.category.data== "all":
            myquery = {"Price":{"$lt":form.price.data}}
        else:
            myquery = {"Price":{"$lt":form.price.data},"category":form.category.data}
        print(myquery)
        mydoc = mycol.find(myquery)
        print (mydoc)
        post=[]
        for x in mydoc:
            post.append(x)
        return render_template('novice.html',title="Product List", posts=post)
    return render_template('index.html',title="Home", form=form)


