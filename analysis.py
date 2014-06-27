import pickle
import numpy
from collections import Counter
from PIL import Image

# s is in the form '(r, g, b)'
def parseRGB(s):
    s = s.replace('(', '').replace(')', '').replace(',', '')
    vals = s.split()
    return (int(vals[0]), int(vals[1]), int(vals[2]))

def main():
    data = pickle.load(open('acc.p', 'rb'))
    created = Image.new("RGB", (101, 100))
    pixels = created.load()

    for (x,y), value in numpy.ndenumerate(data):
        l = Counter(value).most_common(20)
        color, _ = l[min(15, len(l))]
        pixels[x,y] = parseRGB(color)
        print x, y, color

    created.save(open('temp.png'))

main()
