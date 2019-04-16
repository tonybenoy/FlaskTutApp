from app import app,login
from flask import render_template, flash, redirect,url_for,request
from app.forms import NoviceForm ,RegisterationForm,ProForm ,LoginForm ,EditProfileForm, IndexForm #import all the form classes from form.py
import pymongo
from flask_login import login_user,current_user,UserMixin,logout_user,login_required # Login and session management 
from werkzeug.security import generate_password_hash,check_password_hash #To generate and check password hashes in database
from werkzeug.urls import url_parse
from bson.objectid import ObjectId #TO search with id in mongo db we need bson object
class User(UserMixin): #Defined user object  for session management. If using ORM then you should define all the object but not required as we are using Direct connections to mongo
    pass


def choicesgenerator(items):
    a = [("All","All")]
    if items == None:
        a.append("None Available", "None Available")
    else:
        for item in items:
            a.append((item, item))
    return a

@login.user_loader # Used to load a user in login manager defined in __init__.py Define all user related items here as current logged in user object
def load_user(id):
    user = User()
    user.id = id
    return user

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
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = IndexForm()
    if form.validate_on_submit(): #when form is submitted then this block of code will be run i.e. on POST
         return redirect(url_for('search',usertype=form.usertype.data))
    return render_template('index1.html',title="Home", form=form) #Pass the form object on top if it is a GET request
    
 
@app.route('/search/<usertype>', methods=['GET', 'POST'])
def search(usertype):
    if usertype == "n":
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["novicedataset"]
        form = NoviceForm(choicesgenerator(mycol.find({}).distinct("category"))) #create and object of the form class
        myclient.close()
    elif usertype == "p":
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["ram"]
        ramchoice = choicesgenerator(mycol.find({}).distinct("ram"))
        mycol = mydb["cpu"]
        cpuchoice = choicesgenerator(mycol.find({}).distinct("cpu"))
        mycol = mydb["gpu"]
        gpuchoice = choicesgenerator(mycol.find({}).distinct("GPU"))
        mycol = mydb["motherboard"]
        motherboardchoice = choicesgenerator(mycol.find({}).distinct("mb"))
        mycol = mydb["hdd"]
        hddchoice = choicesgenerator(mycol.find({}).distinct("hdd"))
        mycol = mydb["powersupply"]
        powersupplychoice = choicesgenerator(mycol.find({}).distinct("powersupply"))
        form = ProForm(ramchoices=ramchoice, cpuchoices=cpuchoice, gpuchoices=gpuchoice, powersupplychoices=powersupplychoice, hddchoices=hddchoice, motherboardchoices=motherboardchoice)
    if form.validate_on_submit(): #when form is submitted then this block of code will be run i.e. on POST
        #Create a connection everytime and do not use global connections.
        if usertype== "n":
            myclient = pymongo.MongoClient("mongodb://localhost:27017")
            mydb = myclient["mydatabase"]
            mycol = mydb["novicedataset"]
            if form.category.data== "All": # To do a global search on all categories
                myquery = {"Price":{"$lt":form.price.data}} #$lt for less than 
            else:
                myquery = {"Price":{"$lt":form.price.data},"category":form.category.data}
            mydoc = mycol.find(myquery)
            post=[] #List that will be passed to the template to display
            for x in mydoc:
                post.append(x) #Appending all to a list as mydoc is a mongodb object
            myclient.close() # Always close connections 
            #Posts contain the list of dictionary/json information to be displayed
            #This render template will be called after the form submission
            return render_template('novice.html',title="Product List", posts=post) 
        elif usertype == "p":
            myclient = pymongo.MongoClient("mongodb://localhost:27017")
            mydb = myclient["mydatabase"]
            
            mycol = mydb["cpu"]
            if form.cpu.data== "All":
                myquery = {} 
            else:
                myquery = {"cpu":form.cpu.data} #$lt for less than 
            mydoc = mycol.find(myquery)
            cpu=[] #List that will be passed to the template to display
            for x in mydoc:
                cpu.append(x) #Appending all to a list as mydoc is a mongodb object
            
            mycol = mydb["ram"]
            if form.ram.data== "All":
                myquery = {} 
            else:
                myquery = {"ram":form.ram.data} #$lt for less than 
            mydoc = mycol.find(myquery)
            ram=[] #List that will be passed to the template to display
            for x in mydoc:
                ram.append(x) #Appending all to a list as mydoc is a mongodb object
            
            mycol = mydb["gpu"]
            if form.gpu.data== "All":
                myquery = {} 
            else:
                myquery = {"GPU":form.ram.data} #$lt for less than 
            mydoc = mycol.find(myquery)
            gpu=[] #List that will be passed to the template to display
            for x in mydoc:
                gpu.append(x) #Appending all to a list as mydoc is a mongodb object
            
            mycol = mydb["hdd"]
            if form.hdd.data== "All":
                myquery = {} 
            else:
                myquery = {"hdd":form.hdd.data} #$lt for less than 
            mydoc = mycol.find(myquery)
            hdd=[] #List that will be passed to the template to display
            for x in mydoc:
                hdd.append(x) #Appending all to a list as mydoc is a mongodb object
            
            mycol = mydb["motherboard"]
            if form.motherboard.data== "All":
                myquery = {} 
            else:
                myquery = {"mb":form.hdd.data} #$lt for less than 
            mydoc = mycol.find(myquery)
            motherboard=[] #List that will be passed to the template to display
            for x in mydoc:
                motherboard.append(x) #Appending all to a list as mydoc is a mongodb object
            
            mycol = mydb["powersupply"]
            if form.powersupply.data== "All":
                myquery = {} 
            else:
                myquery = {"powersupply":form.hdd.data} #$lt for less than 
            mydoc = mycol.find(myquery)
            powersupply=[] #List that will be passed to the template to display
            for x in mydoc:
                powersupply.append(x) #Appending all to a list as mydoc is a mongodb object
            
            myclient.close()  # Always close connections 
            post=[]
            for cpuitem in cpu:
                for ramitem in ram:
                    for hdditem in hdd:
                        for gpuitem in gpu:
                            for powersupplyitem in powersupply:
                                for motherboarditem in motherboard:
                                    item={
                                        "cpu": cpuitem,
                                        "ram": ramitem,
                                        "hdd": hdditem,
                                        "gpu": gpuitem,
                                        "powersupply": powersupplyitem,
                                        "motherboard":motherboarditem,
                                        "totalprice":float(cpuitem["price"])+float(ramitem["price"])+float(gpuitem["price"])+float(powersupplyitem["price"])+float(hdditem["price"])+float(motherboarditem["price"])
                                    }
                                    post.append(item)
            #Posts contain the list of dictionary/json information to be displayed
            #This render template will be called after the form submission
            return render_template('pro.html',title="Product List",posts=post)
    return render_template('index.html',title="Home", form=form) #Pass the form object on top if it is a GET request

@app.route("/postconf/<lap>", methods=['GET'])
@login_required
def postl(lap):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["mydatabase"]
    mycol = mydb["novicedataset"]
    myquery = {"_id": ObjectId(lap)}
    mylaptop = mycol.find_one(myquery)
    post={"item": mylaptop["name"],
   "price":float(mylaptop["Price"]),
   "userid":current_user.id,
   }
    mycol = mydb["posts"]
    x = mycol.insert_one(post)
    flash('Laptop saved to your Dashboard.')
    myclient.close()
    return redirect(url_for('index'))

@app.route("/postconfig/<cpu>/<ram>/<gpu>/<ps>/<hdd>/<mb>", methods=['GET'])
@login_required
def post(ram, cpu,gpu,mb,ps,hdd):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["mydatabase"]
    mycol = mydb["cpu"]
    myquery = {"_id": ObjectId(cpu)}
    mycpu = mycol.find_one(myquery)
    mycol = mydb["ram"]
    myquery = {"_id": ObjectId(ram)}
    myram = mycol.find_one(myquery)
    mycol = mydb["gpu"]
    myquery = {"_id": ObjectId(gpu)}
    mygpu = mycol.find_one(myquery)
    mycol = mydb["hdd"]
    myquery = {"_id": ObjectId(hdd)}
    myhdd = mycol.find_one(myquery)
    mycol = mydb["powersupply"]
    myquery = {"_id": ObjectId(ps)}
    mypowersupply = mycol.find_one(myquery)
    mycol = mydb["motherboard"]
    myquery = {"_id": ObjectId(mb)}
    mymotherboard = mycol.find_one(myquery)
    
    post={"item": mycpu["name"]+" and "+myram["name"]+" and "+mygpu["name"]+" and "+myhdd["name"]+" and "+mypowersupply["name"]+" and "+mymotherboard["name"] ,
   "price":float(mycpu["price"])+float(myram["price"])+float(mygpu["price"])+float(myhdd["price"])+float(mypowersupply["price"])+float(mymotherboard["price"]),
   "userid":current_user.id,
   }
    mycol = mydb["posts"]
    x = mycol.insert_one(post)
    flash('Config saved to your Dashboard.')
    myclient.close()
    return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated: #User to check if there is user currently a user that is logged in. Use this to check the user logged in status. Done to disable registration page for logged in user.
        return(url_for('index'))
    form = RegisterationForm()
    if form.validate_on_submit():
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        myquery = {"email":form.email.data}
        mydoc = mycol.find_one(myquery) #Using find_one as unless externally inserted there won't be multiple records. If using find then implement count. 
        """
        Checking if email already used
        """
        if mydoc:
            flash('Email address already exist!') #Flashes error message on the page
            myclient.close()
            return redirect(url_for('register')) #redirects to the function/method
        """
        Checking if username already used
        """
        myquery = {"username":form.username.data}
        mydoc = mycol.find_one(myquery)
        if mydoc:
            flash('Username already exist!')
            myclient.close()
            return redirect(url_for('register'))
        hashedpass = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=12) #Encrypting password. Never store plaintext passwords
        mydict = { "username":form.username.data, "email": form.email.data,"password":hashedpass}
        x = mycol.insert_one(mydict)  #Adding user to mongo DB
        flash('Congratulations, you are now a registered user!')
        myclient.close()
        return redirect(url_for('login')) # Redirect to login
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
@login_required #Every url that you want to lock behind a Login use this decorator
def logout():
    logout_user() #Logs out the user session
    return redirect(url_for('index')) 

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated: #same as before
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        myquery = {"username":form.username.data}
        mydoc = mycol.find_one(myquery)
        myclient.close()
        if mydoc == None: #If no user found
            flash('Username not found! Do you want to register?')
            return redirect(url_for('login'))
        else:
            if check_password_hash(mydoc["password"], form.password.data) == False: # Comparing password hashes
                flash('Invalid Password')
                return redirect(url_for('login'))
            else:
                user = User() #User object needed for odoo session management
                user.id = mydoc["_id"] # Always use an ID to create a logged in user to be used as a primary key
                user.name = form.username.data # Can also use from passed["username"]
                login_user(user, remember = form.remember_me.data) #remember allows you to stay logged in even after you close the browser
                next_page = request.args.get('next') # If there is a url that the user came with /user/abc but as it has login required decorated he/she won't be able to access it ,therefore next url will be /user/abc . 
                if not next_page or url_parse(next_page).netloc != '': #If no next url or location load index
                    next_page = url_for('index')
                return redirect(next_page) 
    return render_template('login.html',title='Sign In', form=form)

@app.route('/dashboard') # Passing parameters through url/route
@login_required
def user(): #Parameter in url passed in function must have same var name
    user=User() 
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["mydatabase"]
    mycol = mydb["users"]
    myquery = {"_id": ObjectId(current_user.id)}
    mydoc = mycol.find(myquery)
    for item in mydoc:
        user.username = item["username"]
        user.id = item["_id"] # This is done so that in the template you can enable edit button if the user is seeing his profile
    myclient.close()
    mycol = mydb["posts"]
    myquery = {"userid": current_user.id}
    mydoc = mycol.find(myquery)
    posts=[]
    for item in mydoc:
        posts.append(item)
    return render_template('user.html', user=user,posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        myquery = {"_id": ObjectId(current_user.id)} #bson objectid to search with id
        newvalues = { "$set": { "username": form.username.data } }
        mycol.update_one(myquery, newvalues) # Mongo db update
        myclient.close()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET': #checking if get method
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["mydatabase"]
        mycol = mydb["users"]
        myquery = {"_id": ObjectId(current_user.id)}
        mydoc = mycol.find_one(myquery)
        form.username.data = mydoc["username"] #if it is a get request prefill the form with data to be edited
        myclient.close()
    return render_template('edit_profile.html', title='Edit Profile',form=form)
