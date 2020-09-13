import os

basedir = os.path.abspath(os.path.dirname(__file__)) #This line just gets the dir this file is located

class Config(object):

    SECRET_KEY = 'shhh-dont-tell-anyone' # keep this safe in deployment

    # SQL database config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


