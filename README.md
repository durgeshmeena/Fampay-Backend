# Fampay-Backend Assignment -Extern

# Project Goal
 To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
# Basic Requirements:
-Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of vid eos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

-A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

-It should be scalable and optimised.

# To Run the project:
 
## step 1 :  
create `.env` file containg <br>
```  SECRET_KEY=''
  MONGO_URI='mongodb+srv://'
  YOUTUBE_API_URL='https://www.googleapis.com/youtube/v3/search/'
  GOOGLE_API_KEY=''
```    
  
  
## step 2 : 
  Download required libraries by `pip install -m requirements.txt`<br>
  
## step 3 : 
  Start project using batchfile
  in `cmd` enter `run`

# References
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(38).png
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(39).png
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(40).png
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(41).png
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(42).png
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(43).png
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(44).png
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(45).png
https://github.com/durgeshmeena/Fampay-Backend/blob/assets/Screenshot%20(46).png


