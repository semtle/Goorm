#!/usr/bin/env python
"""
Image-colored wordcloud
========================
You can color a word-cloud by using an image-based coloring strategy implemented in
ImageColorGenerator. It uses the average color of the region occupied by the word
in a source image. You can combine this with masking - pure-white will be interpreted
as 'don't occupy' by the WordCloud object when passed as mask.
If you want white as a legal color, you can just pass a different image to "mask",
but make sure the image shapes line up.
"""

from os import path
from PIL import Image
import numpy as np

from cloud import WordCloud, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'clou/test/braid.txt')).read()
alice_coloring = np.array(Image.open(path.join(d, "examples/alice_color.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

