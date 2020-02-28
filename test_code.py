from image_handler import check_dir
import globals
import os
import shutil
import glob
import time
#import keys
import threading
from twitter_handler import get_screen_name,all_tweets,delete_all, all_tweets_test
from video_handler import image2vid, make_dir_video
from image_handler import check_dir, format_tweet_text, getImage,tweet_video,make_dir



iskey = False
tweet_flag = False
 #checking for key file. 
if os.path.isfile(os.getcwd() + "/keys") == True:
    iskey = True
    shutil.copy('keys', 'keys.py')
    from keys import *

#******** BELOW TESTS ONLY WORK IF THERE IS A KEYS FILE*********
    
#test if the function is returning tweets
def test_all_tweets():
    if iskey:
        all_tweets = all_tweets_test("NPR")
        length = len(all_tweets)
        tweet_flag = True
        assert length != 0
    else:
        assert 1==1
        #check if the function is returning images
def test_tweet_image():
    if iskey:
        all_tweets = all_tweets_test("NPR")
        tweet_video(all_tweets, "NPR", 0)
        if os.path.isfile(os.getcwd() + '/MyImages'+'/NPR'):
            assert 1==1
        else:
            assert 1==0
           # tweet_flag = False
 #check if function is returning video           
def test_tweet_video():
    if iskey:
        all_tweets = all_tweets_test("NPR")
        tweet_video(all_tweets, "NPR", 0)
        path = make_dir("NPR")
        image2vid(path, "NPR")
        if os.path.isfile(os.getcwd() + '/MyVids'+'NPR.mp4'):
            assert 1==1
        else:
            assert 1==0            
def test_no_tweets():
    if iskey:
        all_tweets = all_tweets_test("rzaveri8")
        length = len(all_tweets)
        assert length!=0 
    else:
        assert 1==1   






        









