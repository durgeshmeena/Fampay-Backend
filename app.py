from flask import Flask

# loading .env file which stores PROJECT SECRETE_KEYS
from os import environ
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# importing controler functions
from user.task import query, search, start
import asyncio


SECRET_KEY = environ.get('SECRET_KEY')

app = Flask(__name__)
app.secret_key = SECRET_KEY

# route for home page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# route for quering database
@app.route("/query")
@app.route("/query/<page>")
def query_DB(page=1):
    return query(page)
       
    
# route for searching title and discription of videos
@app.route("/search")
@app.route("/search/<tag>")
def search_DB(tag=''):
    print(tag)
    data = search(tag)
    return data    

# route for start fetching latest videos from Youtube
@app.route("/start")
def strt():
    asyncio.run(start())
    return "S"
