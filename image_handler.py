import requests
import os
import tweepy
#import pandas as pd
import csv
import datetime
import time
import json
import math
from PIL import Image
from PIL import ImageDraw
from io import BytesIO
import threading
from multiprocessing import Queue, current_process




def format_tweet_text(text):
    #tweet wrapper function
    if len(text) > 35:
        i = 0
        res = '\n'.join(text[i:i + 35] for i in range(0, len(text), 35))
        return res
    else:
        return text


def getImage(tweet, image):
    url = tweet.entities['media'][0]['media_url_https']
    bytes =  requests.get(url)
    photo = Image.open(BytesIO(bytes.content))
    image.paste(photo, (10, 130))

def tweet_video(all_tweets, screen_name, vid_id):
    index = 0
    for tweet in all_tweets:
        path = make_dir(screen_name)
        if (datetime.datetime.now() - tweet.created_at).days < 1:
            wrapped_text = format_tweet_text(tweet.full_text)
            img_height = 200
            img = Image.new('RGB', (300, img_height), (255, 255, 255))
            d = ImageDraw.Draw(img)
            d.text((10, 10), wrapped_text.encode(
                'cp1252', 'ignore'), fill=(0, 0, 0))
        # IF THERE IS AN IMAGE
            if 'media' in tweet.entities:
                    getImage(tweet, img)
            image_name = "tweet" + str(index) + ".png"
            img.save(path + image_name)
            index += 1

def check_dir(path): #from https://thispointer.com/how-to-create-a-directory-in-python/
    try:
        os.mkdir(path)
    except OSError:
        print ("directory %s already exists" % path)  
    else:
        print ("Successfully created the directory %s " % path)
    return True

def make_dir(screen_name):
    # create directories for images.
    check_dir(os.getcwd()+ "/MyVids")
    path = os.getcwd()+ "/MyImages"
    check_dir(path)
    path = path + '/' + screen_name + '/'
    check_dir(path)
    return path

    

      


# NEED Function To remove all previous videos etc....
# if it exists then delete it and recreate it. 
    


