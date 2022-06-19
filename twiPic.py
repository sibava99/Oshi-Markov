# coding: UTF-8
from random import sample
from unittest import removeResult
from genePic import img_add_msg
import os
from dotenv import load_dotenv
import tweepy
import requests
import re
import cv2
from PIL import Image, ImageFont, ImageDraw

def getPic(Account):
    load_dotenv()
    consumer_key = os.environ["consumer_key"]
    consumer_secret = os.environ["consumer_secret"]
    access_token = os.environ["access_token"]
    access_token_secret = os.environ["access_token_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    img = api.get_user(screen_name = Account)
    url = img.profile_image_url
    url = re.sub('_normal.','.', url)
    dst_path = './' + str(Account) + '.png'
    response = requests.get(url)
    image = response.content
    return image

def img_add_msg(img, icon):
    height, width, channels = img.shape[:3]                 #大きさ取得
    #print("width: " + str(width))
    #print("height: " + str(height))
    draw = ImageDraw.Draw(img)                          # 描画用のDraw関数を用意
    positionx = width/2 - 450
    positiony = height/2 -100

    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    draw.text((positionx, positiony), message, font=font, fill=(0,0,0, 0))
    img = np.array(img)                                 # PIL型の画像をcv2(NumPy)型に変換
    return img                                          # 文字入りの画像をリターン
   
Account = input()

#with open("wawawa.png", "wb") as f:
#        f.write(getPic(Account))

img = cv2.imread('front\src\pic\mob.jpg', 1)                         # カラー画像読み込み
cv2.imwrite('output.jpg', img)
