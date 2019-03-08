from app import app
from flask import render_template
from app.forms import NoviceForm #import all the form classes from form.py
import pymongo

"""Use @app.route to define urls. 
If you want a url like localhost:5000/joe
then define  @app.route('/joe'). Methods 
are used to define http methods that can
be used with the that endpoint/url.
If you have a form use ['GET','POST'].
If you are just displaying just use POST
Define the function which has to be called 
after the @api.route 
"""
@app.route('/',methods=['GET','POST']) 
@app.route('/index',methods=['GET','POST'])
def index():
    form = NoviceForm() #create and object of the form class
    if form.validate_on_submit(): #when form is submitted then this block of code will be run i.e. on POST
        #Create a connection everytime and do not use global connections.
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["novicedataset"]
        if form.category.data== "all": # To do a global search on all categories
            myquery = {"Price":{"$lt":form.price.data}} #$lt for less than 
        else:
            myquery = {"Price":{"$lt":form.price.data},"category":form.category.data}
        mydoc = mycol.find(myquery)
        post=[] #List that will be passed to the template to display
        for x in mydoc:
            post.append(x) #Appending all to a list as mydoc is a mongodb object
        myclient.close() # Always close connections 
        """Posts contain the list of dictionary/json information to be displayed
        This render template will be called after the form submission
        """
        return render_template('novice.html',title="Product List", posts=post) 

    return render_template('index.html',title="Home", form=form) #Pass the form object on top if it is a GET request


