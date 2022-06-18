"""
python learn.py <filename> [format] [max_chars] [min_chars]
filename: Do not include .txt or .json etc.
"""
from random import sample
from unittest import result
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

logger = logging.getLogger(__name__)
fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)

args = sys.argv

#サーバとローカルどちらでも動作する形
#テキストと最長出力長と最小出力長を入力して、モデルを保存し、保存したディレクトリを返す
def study_from_markov(text):
    n = 1
    text = markov.parse_text(text)
    #format = format
    max_chars = 75
    min_chars = 10
    #logger.info('Parsed text.')
    #text_model = markov.build_model(text, format=format, state_size=2)
    text_model = markov.build_model(text, state_size=2)
    try:
        for _ in range(n):
            sentence = markov.make_sentences(text_model, start='', max=max_chars, min=min_chars)
            #logger.info(sentence)
    except KeyError:
        #logger.error('KeyError: No sentence starts with "start".')
        #logger.info('If you set format=True, please change "start" to another word.')
        #logger.info('If you set format=False, you cannot specify "start".')
        pass
    return sentence

#print('Usage: python learn.py <filename> [format] [max_chars] [min_chars]')
#print('Usage: python learn.py <filename> [max_chars] [min_chars]')

# .envファイルの内容を読み込見込む
load_dotenv()
max_chars = int(args[2]) if args[2:3] else 70
min_chars = int(args[3]) if args[3:4] else 25

if args[1] == '^@*.':
    tweets = getTweet(Account)
    
try:
    filename = args[1]
    filepath = 'data/' + filename + '.txt'
    text = open(filepath, 'r').read()
    #format = bool(strtobool(args[2])) if args[2:3] else True

    #parsed_text = generate_sentence(text, format, max_chars, min_chars)
    print(study_from_markov(text, max_chars, min_chars))
    #text = generate_from_markov(path)
except IndexError:
    print('ERROR: filename is required. (e.g. "sample")')
    sys.exit()


"""
1. Load text -> Parse text using MeCab
"""
#parsed_text = markov.parse_text('data/' + filename + '.txt')

"""
2. Build model
"""

# Load from JSON
# json = open('input.json').read()
# text_model = markovify.Text.from_json(json)


"""
3. Make sentences
"""
