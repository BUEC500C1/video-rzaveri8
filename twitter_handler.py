import requests
import config
import os
import tweepy
#import pandas as pd
import csv
import datetime
import time
import json



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

class Tweet():
    def init(self,user,text,images):
        self.name = name
        self.text = text
        self.images = images

    def json(self):
        return{"user":self.name,"text":self.text,"images":self.images}


def all_tweets(screen_name):
    new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode = "extended")
    return new_tweets


def get_tweets(new_tweets):
    today_tweets = []
    a = open('tasksJSON', 'w')
    for tweet in new_tweets:
        #print datetime.datetime.now() - tweet.created_at
        #print tweet.fu
        if (datetime.datetime.now() - tweet.created_at).days < 1:
            text = tweet.full_text
            user = tweet.user.screen_name
            images = []
            if 'media' in tweet.entities:
                for image in tweet.entities['media']:
                    if(image['type'] == 'photo'):
                        images.append(image['media_url'])
            my_tweet = {"user":tweet.user.screen_name,"text":tweet.full_text,"images":images}
            today_tweets.append(my_tweet)
    return today_tweets


temp =  all_tweets('NatGeo')
json = get_tweets(temp)

print json
