import os
"""
def convert_images_to_video(image_path, video_id):
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "panic",
           "-f", "image2", "-i", f"{image_path}/tweet%d.png",
           "-preset", "ultrafast",
           "-r", "1/3", "-y", f"./videos/{video_id}.ogg"]
    p = Popen(cmd)
    p.communicate()
 """

def convert_images_to_video(image_path, screen_name):
    cmd = 'ffmpeg -start_number n -i' +image_path+' test_%d.jpg -vcodec mpeg4 test.avi'


   # cmd = 'ffmpeg -framerate 5 -i'+image_path+'/tweet%d.png myvideo.mp4'

    #cmd = 'ffmpeg
    #  -r 1 -i '+image_path+'tweet%d.png -vcodec mpeg4 -y /'+screen_name+'.mp4'
    os.system(cmd)


#ffmpeg -framerate 5 -i img-%02d.png myvideo.mp4
