#!/usr/bin/env python

from os import path
from PIL import Image
from goorm import WordCloud

import sys
import argparse
import numpy as np

d = path.dirname(__file__)

# Read the whole text.

try:
    textfile = str(sys.argv[1])

except:
    print("Text =  data/text/, Template = data/tmeplate/") 
    print("Usage: goorm.py text_file.txt mask_image.jpg")
    sys.exit(1)

try:
    imagefile = str(sys.argv[2])

except:
    print("default template has choosed")
    imagefile = "default.png"


# read text
text = open(path.join(d, 'data/text/%s' % textfile)).read()

# read the mask image
mask = np.array(Image.open(path.join(d, "data/template/%s" % imagefile)))

# settings
wc = WordCloud(background_color="white", max_words=500, mask=mask)

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "data/output.png"))
