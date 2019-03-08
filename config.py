import os
class Config(object): #Add all app related config in here
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'APPPASSWORD' #Used to keep all data safe by preventing CSRF
    #os.environ is used to het the key from the Operating system variable