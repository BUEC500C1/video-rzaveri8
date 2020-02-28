import os
from image_handler import check_dir
import threading
from shutil import rmtree
from multiprocessing import Queue

work_queue = Queue()
work_progress = {}

def work_dispatcher(process_pool):
    while True:
        video_id, user = work_queue.get()
        path = make_dir_video(user)
        print("working")
        process_pool.apply_async(image2vid, args=(video_id, path, user))

def make_dir_video(screen_name):
    # create directories for images.
    check_dir(os.getcwd()+ "/MyVids")
    path = os.getcwd()+ "/MyVids"
    check_dir(path)
    path = path + '/'
    check_dir(path)
    return path

def image2vid(image_path, screen_name):

    vidpath = make_dir_video(screen_name)

    cmd = "ffmpeg -r 1/3 -f image2 -s 300x300 -i " +image_path+ "tweet%d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p "+vidpath+screen_name+".mp4"
    os.system(cmd)


