from flask import Flask, redirect, request, send_file, render_template
import os.path
import os
import signal
import threading
from multiprocessing.pool import ThreadPool
from twitter_handler import get_screen_name,all_tweets
from video_handler import image2vid, make_dir_video
from image_handler import check_dir
from image_handler import format_tweet_text, getImage,tweet_video,make_dir

import globals

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return render_template('status.html', calls = globals.processes)

@app.route('/video/<name>')
def watchVideo(name):
    vid_path = make_dir_video(name)
    #clean_old()
    call = {
        "user_name": name,
        "id": globals.id,
        "status": "queued"
    }
    vid_id = str(globals.id)
    globals.id = globals.id +1

    globals.processes[vid_id] = call
    globals.q.put(call)
    globals.q.join()
    return send_file(vid_path + name+".mp4")

if __name__ == '__main__':
    globals.init()
    globals.q.join()
    threads = []
    for i in range (globals.max_threads):
        worker = threading.Thread(target=all_tweets)
        worker.setDaemon(True)
        threads.append(worker)
    for t in threads:
        t.start()    
    #watchVideo(user)
    app.run(debug=True)
   