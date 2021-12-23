import requests
from user.db import configDB
from flask import jsonify

from os import environ
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import time
import asyncio

YOUTUBE_API_URL = environ.get('YOUTUBE_API_URL')
GOOGLE_API_KEY = environ.get('GOOGLE_API_KEY')

db = configDB()


     


async def video_data():
    page_token = ""
    # k=5  
    while True:
        # k = k-1
        params = {
            "part":"snippet",
            "maxResults":50,
            "type":"video",
            "key":GOOGLE_API_KEY,
            "pageToken":page_token,
            "publishedAfter":"2020-01-01T00:00:00Z",
            "order":"date",
            "q":"Bollywood Music"
            
        }

        response = requests.get(YOUTUBE_API_URL, params=params)
        print(response)
        DATA_LIST = []
        if response.status_code == 200:
            json_response = response.json()
            if json_response.get('nextPageToken'):
                page_token = json_response['nextPageToken']
            else:
                page_token = ''
                # k=1    
            for i in json_response.get("items", []):
                video_id = i.get("id", {}).get("videoId")
                snippet_data = i.get("snippet", {})
                if snippet_data:
                    # print(i)
                    
                    Id = video_id
                    Title = str(i['snippet']['title'])
                    
                    Description = i['snippet']['description']
                    # Publishing_datetime = dateparser.parse(i['snippet']['publishedAt'])
                    Thumbnails_urls = i['snippet']['thumbnails']['default']['url']


                    DATA  = {
                        '_id' : Id,
                        'Title' :  Title,
                        'Description' : Description,
                        'Thumbnails_urls' : Thumbnails_urls,
                        'publishTime' : i['snippet']['publishTime'],

                    }   

                    # print(DATA)
                    DATA_LIST.append(DATA)

           
            for d in DATA_LIST:
                time.sleep(2)
                if db.find_one({"_id":d["_id"]}):
                    print('duplicate data')
                else:
                    r=db.insert_one(d)
                    print("Youtube data saved to database!!")
                    print(r.inserted_id)
        time.sleep(10)  
          

async def start():
    loop = asyncio.get_event_loop()
    print('loop started')
    loop.run_forever(await video_data())