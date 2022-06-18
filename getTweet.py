# coding: UTF-8
from random import sample
from unittest import result
import tweepy
import MeCab
import unidic
import re
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()



def getTweet(Account):
    consumer_key = os.environ["consumer_key"]
    consumer_secret = os.environ["consumer_secret"]
    access_token = os.environ["access_token"]
    access_token_secret = os.environ["access_token_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    result = api.user_timeline(screen_name = Account, count = 3000)
    tweets = []
    for i in result:
        tweet = i.text
        tweets.append(tweet)
    return tweets

Account = input()
tweets = getTweet(Account)

with open('dataset.txt',mode='w', encoding='utf-8') as f:
    for tweet in tweets:
        f.write(tweet)

with open ('dataset.txt',mode='r', encoding='utf-8') as f:
	text = f.read()
	text = re.sub('http.*','', text)
	text = re.sub('　','', text)
	text = re.sub(r'\(.*?\)','',text)
	text = re.sub(r'\*\d*','',text)
	text = re.sub('RT.*','',text)
	text = re.sub('@.*','',text)

with open('output.txt',mode='w', encoding='utf-8') as f:
    f.write(text)