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

