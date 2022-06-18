"""
python learn.py <filename> [format] [max_chars] [min_chars]
filename: Do not include .txt or .json etc.
"""
from random import sample
from unittest import result

from torch import save
import tweepy
import MeCab
import unidic
import re
import os
from dotenv import load_dotenv
import markov
import logging
import sys
from distutils.util import strtobool
import markovify

#サーバとローカルどちらでも動作する形
#テキストと最長出力長と最小出力長を入力して、モデルを保存したjsonファイルを返す
def study_from_markov(text):
    text = markov.parse_text(text)
    text_model = markov.build_model(text, state_size=2)
    json = text_model.to_json()
    return json

#ツイッターアカウントを入力して、モデルを保存したjsonファイルを返す
def getTweet(Account):
    consumer_key = os.environ["consumer_key"]
    consumer_secret = os.environ["consumer_secret"]
    access_token = os.environ["access_token"]
    access_token_secret = os.environ["access_token_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    result = api.user_timeline(screen_name = Account, count = 3000)
    tweets = ""
    for i in result:
        tweets += i.text
    text = re.sub('http.*','', tweets)
    text = re.sub('　','', text)
    text = re.sub(r'\(.*?\)','',text)
    text = re.sub(r'\*\d*','',text)
    text = re.sub('RT.*','',text)
    text = re.sub('@.*','',text)
    print(text)
    text = markov.parse_text(text)
    text_model = markov.build_model(text, state_size=2)
    json = text_model.to_json()
    
    return json
    
#モデルが保存されてるjsonファイルを渡し、最短長以上最長長以下の文章を生成する
def generate_from_markov(path, max_chars, min_chars):
    text_model = markovify.Text.from_json(json)
    try:
        for _ in range(10):
            sentence = markov.make_sentences(text_model, start='', max=max_chars, min=min_chars)
            logger.info(sentence)
    except KeyError:
        pass
    return sentence

# .envファイルの内容を読み込見込む
if __name__ == '__main__':
    max_chars = 70
    min_chars = 15
    logger = logging.getLogger(__name__)
    fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
    logging.basicConfig(level=logging.DEBUG, format=fmt)

    args = sys.argv
    load_dotenv()
    max_chars = int(args[2]) if args[2:3] else 70
    min_chars = int(args[3]) if args[3:4] else 25
    res = re.match('^@', args[1])
    
    if res:
        json = getTweet(args[1])
        print(generate_from_markov(json, max_chars, min_chars))
    
    else:
        try:
            filename = args[1]
            filepath = 'data/' + filename + '.txt'
            text = open(filepath, 'r').read()
            json = study_from_markov(text)
            print(generate_from_markov(json, max_chars, min_chars))
        except IndexError:
            print('ERROR: filename is required. (e.g. "sample")')
            sys.exit()
    
    try:
        filename = args[1]
        filepath = 'data/' + filename + '.txt'
        text = open(filepath, 'r').read()
        json = study_from_markov(text)
        print(generate_from_markov(json, max_chars, min_chars))
    except IndexError:
        print('ERROR: filename is required. (e.g. "sample")')
        sys.exit()