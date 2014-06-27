from PIL import Image
import os
from collections import Counter
import numpy
import pickle

dir = 'test_landscape'

width = 101
height = 100

acc = numpy.empty([width, height], dtype=list)
acc.fill([])

for filename in os.listdir(dir):
    if 'test_' not in filename:
        pass

    image = Image.open(os.path.join(dir, filename))
    pixels = image.load()

    for i in range(0, image.size[0]):
        for j in range(0, image.size[1]):
            color = str(pixels[i,j])
            temp = list(acc[i][j])
            temp.append(color)
            acc[i][j] = temp

pickle.dump(acc, open('acc.p', 'wb'))
