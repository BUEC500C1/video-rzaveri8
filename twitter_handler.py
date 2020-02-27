import requests
import config
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


# Consumer keys and access tokens, used for OAuth
consumer_key = config.consumer_key()
consumer_secret = config.consumer_secret()
access_token = config.access_token()
access_token_secret = config.access_token_secret()

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


def get_screen_name(screen_name):
    return screen_name

def tweet_error(screen_name,vid_id): #CHANGE THIS UP.
    error_image = Image.new('RGB', (203, 350), (255, 255, 255))
    d = ImageDraw.Draw(error_image)
    d.text((15, 10), "This user has no tweets", fill=(0, 0, 0))
    error_image.thumbnail((300, 300), Image.ANTIALIAS)
    # saves the image
    image_name = str(vid_id) + screen_name + "_tweet0.png"
    error_image.save(image_name)

def all_tweets():
    while True:
        vid_req = globals.q.get()
        vid_id =  vid_req["id"]
        screen_name = vid_req["user_name"]
        globals.processes[str(vid_id)]["status"] = "processing"
        try:
            new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode = "extended")
        except:
            tweet_error(screen_name, vid_id)
        else:
            tweet_video(new_tweets, screen_name, vid_id)
        #vid_path =  make_dir_video(screen_name)
        im_path = make_dir(screen_name)   
        image2vid(im_path,screen_name)
        globals.processes[str(vid_id)]["status"] = "completed"
        globals.q.task_done()   

# removes all previous tweets, images, and videos
def clean_all():
    for file in os.listdir('.'):
        if file.endswith('.png') or file.endswith('.mp4'):
            os.remove(file)

# cleans all old images out (videos stay)
"""
def clean_old():
    for call in globals.processes.values():
        if call["status"] == "completed":
            for file in os.listdir('.'):
                if file.startswith(str(call["id"]) + call["screen_name"]) & file.endswith('.png'):
                    os.remove(file)          
"""