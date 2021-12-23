from flask import Flask

from os import environ
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from user.task import query, search, start
import asyncio


SECRET_KEY = environ.get('SECRET_KEY')

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/query")
@app.route("/query/<page>")
def query_DB(page=1):
    return query(page)
    
@app.route("/page")
@app.route("/page/<p>")
def test(p=1):
    return str(p)   
    

@app.route("/search")
@app.route("/search/<tag>")
def search_DB(tag=''):
    print(tag)
    data = search(tag)
    return data    

@app.route("/start")
def strt():
    asyncio.run(start())
    return "S"
