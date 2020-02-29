# HW4 EC500
By: Ruby Zaveri

## Main Exercise
Using the twitter feed, construct a daily video summarizing a twitter handle's day.
- Convert text into an image in a frame
- Do a sequence of all texts and images in chronological order.
- Display each video frame for 3 seconds

## Tasks
Establish a processing criteria:
- How many API calls you can handle simultaneously and why?
- For example, run different API calls at the same time?
- Split the processing of an API into multiple threads?

Recommendation for working on the homework:  
### Step 1:
Develop a queue system that can exercise your requirements with stub functions.

This was accomplished by adding each API call to a processing queue. The queue contains a unique id associated with the request. Each process is associated with a single thread that executes requests. The threads all exectue the ```all_tweets``` function, the thread calls form the processing queue and calls other functions that help to transform tweets to videos. 

The ```/video/<name>``` route will return the result of the  ```image2vid``` function. 

And each call the main directory is wiped using the ```delete_all``` function to prevent duplicates in the system. 

### Step 2: 
Develop the twitter functionality with an API

This was accoplished using flask and the tweepy api. The function ```all_tweets``` returns an array of all of the tweets from the current day of the given username. If there are no tweets the webpage returns an error. 

### Step 3:
Integrate them

Include tracking interface to show how many processes are going on and success of each

This was accomplished by having a ```/status ``` route that returns the status of each API call - processing, queuing or finished. 

### Prerequisites

Setup your config /config.py file as shown

```
TWITTER_API_KEY = XXXXXXXXX
TWITTER_API_SECRET_KEY = XXXXXXXXXXXXXXXXXX
TWITTER_ACCESS_TOKEN = XXXXXXXXX
TWITTER_ACCESS_TOKEN_SECRET = XXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### Installing

Install requirements
```
pip3 install -r requirements.txt
```

### Running the Program
Run the command
```
python3 api.py
```
Then navigate to http://127.0.0.1:5000/video/Tweeter_Handle_Here
Please make sure to put a twitter handle in the url or you will get an error. 

To track the progress of the API calls please go to http://127.0.0.1:5000/status


### Tests

To test the program run

```
pytest test_code.py
```
If you do not have a keys file the tests will not run as they test api outputs. 
