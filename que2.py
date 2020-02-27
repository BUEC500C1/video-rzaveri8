# rzaveri EC500 HW4
#from multiprocessing import Queue.Queue
import queue
#import queue
import threading
import time
import os
from subprocess import Popen
from flask import Flask, redirect, request, send_file
from multiprocessing import Queue, current_process
from twitter_handler import get_screen_name
from twitter_handler import all_tweets
from video_handler import image2vid, make_dir_video
from image_handler import check_dir
from image_handler import format_tweet_text
from image_handler import getImage
from image_handler import tweet_video
from image_handler import make_dir
import ffmpegWrapper
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

def init():
    global statusQueue
    statusQueue = {}

workerQ = queue.Queue()

def workerDispatcher():
    """
    Generates Queue that handles creation and deletion 
    of work based on CPU core count.
    """
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        while True:
            hash, handle = workerQ.get()
            executor.submit(image2vid, hash, handle)

    

#if __name__ == '__main__':
    #watchVideo(user)
    #tweets = ["NPR", "NatGeo"]
    #main(tweets)

