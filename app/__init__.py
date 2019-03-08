from flask import Flask
from config import Config #Import configuration from config.py. Optional but good practice
app = Flask(__name__) #creating the app object
app.config.from_object(Config) #Applying config to app
from app import routes #Importing all routes from routes.py
