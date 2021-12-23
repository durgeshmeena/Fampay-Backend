import pymongo
from os import environ, path
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

mongoURI = environ.get('MONGO_URI')

def configDB():
    print('connecting to database...')
    client = pymongo.MongoClient(mongoURI, serverSelectionTimeoutMS=30000)
    database = client.get_database('YoutubeData')
    db = database.ysearch 
    print('Connected to Database!!')
    return db  