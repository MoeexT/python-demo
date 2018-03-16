#! python3
# encoding=utf-8

import numpy as np
from os import path
from PIL import Image
import jieba
import jieba.analyse as analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# text = open('Maraba.txt').read()
alice_coloring = np.array(Image.open("logo1024.jpg"))
stopwords = set(STOPWORDS)
stopwords.add("said")

def chinese():
	string = ""
	with open('hotWords.txt', 'r', encoding='gbk') as f:
		for i in f:
			string += i
	liction = analyse.textrank(string, topK=50, withWeight=True)
	keywords = {}
	for word in liction:
		keywords[word[0]] = word[1]
		
	return keywords
		
wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
				stopwords=stopwords, max_font_size=80, min_font_size=2, 
				# font_path='CabinSketch-Bold.ttf',
				random_state=42)
				
#wc.generate(text)
wc.generate_from_frequencies(chinese())

image_colors = ImageColorGenerator(alice_coloring)

plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
wc.to_file('weibo_logo1024.jpg')
plt.show()
'''

plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
'''