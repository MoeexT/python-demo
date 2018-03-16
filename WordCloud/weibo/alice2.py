#! python3

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


text = open('txt/Maraba.txt').read()

alice_coloring = np.array(Image.open("sb.jpg"))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
				stopwords=stopwords, max_font_size=80, min_font_size=5, 
				font_path='CabinSketch-Bold.ttf',
				random_state=42)
wc.generate(text)

image_colors = ImageColorGenerator(alice_coloring)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
#wc.to_file('sb1.png')

plt.figure()
wc2 = wc.recolor(color_func=image_colors)
plt.imshow(wc2, interpolation="bilinear")
plt.axis("off")
#wc2.to_file('sb2.png')

plt.show()
'''

plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
'''