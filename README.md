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
### Step 2: 
Develop the twitter functionality with an API
### Step 3:
Integrate them
Include tracking interface to show how many processes are going on and success of each

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
Then navigate to http://127.0.0.1:5000/video/'TWITTER HANDLE HERE'
Please make sure to put a twitter handle in the url or you will get an error. 

To track the progress of the API calls please go to http://127.0.0.1:5000/status
