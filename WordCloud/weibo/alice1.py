#! python3

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

# d = path.dirname(r'D:\Sarmon\Documents\Codes\Python\WordCloud\weibo')
# text = open(path.join(d, 'alice.txt')).read()
text = open('txt/Maraba.txt').read()
alice_mask = np.array(Image.open("alice_1.jpg"))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)
wc.generate(text)

# wc.to_file("Maraba.png")

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")

plt.show()