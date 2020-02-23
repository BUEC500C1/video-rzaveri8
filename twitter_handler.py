import requests
import config
import os
import tweepy
#import pandas as pd
import csv
import datetime
import time
import json
from flask import jsonify
import math
from PIL import Image
from PIL import ImageDraw
from io import BytesIO


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

def all_tweets(screen_name):
    new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode = "extended")
    return new_tweets


