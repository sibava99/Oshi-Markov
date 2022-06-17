# coding: UTF-8
import re

with open ('../data/comment.txt',mode='r') as f:
	text = f.read()
	text = re.sub(' ','', text)
	text = re.sub('　','', text)
	text = re.sub(r'\(.*?\)','',text)
	text = re.sub(r'\*\d*','',text)

with open('../data/cleaned_comment.txt',mode='w') as f:
	f.write(text)