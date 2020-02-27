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


def main(tweets):
    #work = q.get()
    def thread():
        while True:
            if q.empty():
                break
            work = q.get()
            print('='*97)
            print("working on {} thread".format(work))
            print()
            #vid_path = make_dir_video(work)
            user = get_screen_name(work)
            all = all_tweets(user)
            path = make_dir(user)
            tweet_video(all,user)
            image2vid(path, user)
            print('='*60)
            print("{} thread done".format(work))
            q.task_done()
            print('now {} threads are running, totally {} threads'.format(threading.activeCount()-2,len(tweets)))
            print('='*60)
    q = queue.Queue()
    for i in tweets:
        q.put(i)
    num_threads = 3
    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=thread)
        t.daemon = True
        threads.append(t)
        t.start()
    q.join() 
    print('all works done')
    

#if __name__ == '__main__':
    #watchVideo(user)
    #tweets = ["NPR", "NatGeo"]
    #main(tweets)

