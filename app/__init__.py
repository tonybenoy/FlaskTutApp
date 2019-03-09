from flask import Flask
from flask_login import LoginManager
from config import Config #Import configuration from config.py. Optional but good practice
app = Flask(__name__) #creating the app object
app.config.from_object(Config)  #Applying config to app
login = LoginManager(app) #LoginManager is user to manage user sessions
login.login_view = 'login' # FOr login object 
from app import routes #Importing all routes from routes.py
