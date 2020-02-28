import requests
from keys import consumer_key, consumer_secret, access_secret, access_token
import os
import tweepy
#import pandas as pd
import csv
import datetime
import time
import json
import threading,queue
import globals
from flask import jsonify, send_file
import math
from PIL import Image
from PIL import ImageDraw
from image_handler import tweet_video,make_dir
from video_handler import image2vid,make_dir_video
import shutil
import glob


# Consumer keys and access tokens, used for OAuth
#consumer_key = config.consumer_key()
#consumer_secret = config.consumer_secret()
#access_token = config.access_token()
#access_token_secret = config.access_token_secret()

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


def get_screen_name(screen_name):
    return screen_name


def all_tweets():
    while True:
        vid_req = globals.q.get()
        vid_id =  vid_req["id"]
        screen_name = vid_req["user_name"]
        globals.processes[str(vid_id)]["status"] = "processing"
        try:
            new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode = "extended")
        except:
            globals.processes[str(vid_id)]["status"] = "Error: No Tweets"
        else:
            tweet_video(new_tweets, screen_name, vid_id)
        #vid_path =  make_dir_video(screen_name)
        im_path = make_dir(screen_name)   
        image2vid(im_path,screen_name)
        globals.processes[str(vid_id)]["status"] = "completed"
        globals.q.task_done()   

# removes all previous tweets, images, and videos
 # removes all previous tweets, images, and videos
def delete_all():
    vid_files = glob.glob(os.getcwd()+ "/MyVids")
    im_files = glob.glob(os.getcwd()+ "/MyImages")
    for file in vid_files:
        shutil.rmtree(file)

    for file in im_files:
        shutil.rmtree(file)    


# cleans all old images out (videos stay)

def delete_old():
    for call in globals.processes.values():
        if call["status"] == "completed":
            im_files = glob.glob(os.getcwd()+ "/MyImages")
            for file in im_files:
                shutil.rmtree(file)         
