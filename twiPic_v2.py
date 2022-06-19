# coding: UTF-8
from email.mime import message
from random import sample
from threading import activeCount
from unittest import removeResult
from genePic import img_add_msg
import os
from dotenv import load_dotenv
import tweepy
import requests
import re
import cv2
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
#import pygame   #pip install pygame
import numpy as np

def paste_image(Account, image1, message):
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
    print(type(image))
    print(type(BytesIO(image)))
    image = Image.open(BytesIO(image))
    print(type(image))
    img = image.resize((400,400))
    print(type(img))
    print(type(image1))
    image1.paste(img,(820,90))
    draw = ImageDraw.Draw(image1)                          # 描画用のDraw関数を用意
    #fnt = ImageFont.truetype('./Kokoro.otf',30) #ImageFontインスタンスを作る、ダウンロードが必要！！！！
    #draw.text((200, 200), message, font=fnt, fill=(0,0,0, 0))
    draw.text((200, 200), message, fill=(0,0,0, 0))
    return image1

Account = "@1000000lome"
message = 'Test Message\nExample'

img = cv2.imread('front\src\pic\mob.jpg', 1)   
print(type(img))                    # カラー画像読み込み
cv2.imwrite('output.jpg', img)

image1 = Image.open('front\src\pic\mob.jpg')
image = paste_image(Account, image1, message)
print("a")
image.save("wawawa.png")