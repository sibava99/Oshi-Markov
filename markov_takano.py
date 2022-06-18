#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from janome.tokenizer import Tokenizer
import markovify

def split(text):
    # 改行、スペース、問題を起こす文字の置換
    table = str.maketrans({
        '\n': '',
        '\r': '',
        '(': '（',
        ')': '）',
        '[': '［',
        ']': '］',
        '"':'”',
        "'":"’",
    })
    text = text.translate(table)
    t = Tokenizer()
    result = t.tokenize(text, wakati=True)
    # 1形態素ずつ見ていって、間に半角スペース、文末の場合は改行を挿入
    splitted_text = ""
    for i in result:
        splitted_text += i 
        if i  != '。' and i  != '！' and i  != '？':
            splitted_text += ' '
        if i  == '。' or i  == '！' or i  == '？':
            splitted_text += '\n'
    return splitted_text

def textGen(text):
    sentence = None
    while sentence == None: # 素材によっては空の文章が生成されることがあるので、その対策
        # テキストを処理できる形に分割
        splitted_text = split(text)

        # モデルの生成
        text_model = markovify.NewlineText(splitted_text, state_size=3)

        # モデルを基にして文章を生成
        for _ in range(10):
            sentence = text_model.make_sentence()   
            if sentence == None: continue
            print(sentence.replace(" ", ""))
    # 学習データの保存
    with open('learned_data.json', 'w', encoding="utf-8") as f:
        f.write(text_model.to_json())

    # データを使いまわす場合
    """
    with open('learned_data.json') as f:
        text_model = markovify.NewlineText.from_json(f.read())
    """

    # 結合された一連の文字列として返す
    return ''.join(sentence.split())

if __name__ == '__main__':
    with open("data/cleaned_comment.txt", "r") as f:
        text = f.read()
    textGen(text)
