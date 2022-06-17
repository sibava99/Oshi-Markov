import logging
import markovify
import MeCab
import re

# Load file
text_file = open("../data/cleaned_comment.txt", "r")
text = text_file.read()

# Parse text using MeCab
parsed_text = MeCab.Tagger('-Owakati').parse(text)

# Build model
text_model = markovify.Text(parsed_text, state_size=2)

# Output
for _ in range(10):
    sentence = text_model.make_short_sentence(100, 20, tries=100).replace(' ', '')
    print(sentence)