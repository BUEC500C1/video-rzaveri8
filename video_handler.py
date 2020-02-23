import os
from image_handler import check_dir
def make_dir_video(screen_name):
    # create directories for images.
    check_dir(os.getcwd()+ "/MyVids")
    path = os.getcwd()+ "/MyVids"
    check_dir(path)
    path = path + '/'
    check_dir(path)
    return path

def convert_images_to_video(image_path, screen_name):
    vidpath = make_dir_video(screen_name)

    cmd = "ffmpeg -r 1/3 -f image2 -s 174x300 -i " +image_path+ "tweet%d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p "+vidpath+screen_name+".mp4"
    os.system(cmd)

