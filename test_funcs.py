from twitter_handler import get_screen_name
from twitter_handler import all_tweets
from video_handler import convert_images_to_video
from image_handler import check_dir
from image_handler import format_tweet_text
from image_handler import getImage
from image_handler import tweet_video
from image_handler import make_dir

user = get_screen_name("NPR")
all = all_tweets(user)
path = make_dir(user)
tweet_video(all,user)
convert_images_to_video(path, user)





