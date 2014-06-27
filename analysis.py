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
    created = Image.new("RGB", (100, 81))
    pixels = created.load()

    for (x,y), value in numpy.ndenumerate(data):
        if x > 99 or y > 80:
            continue
        l = Counter(value).most_common(20)
        color, _ = l[0] if len(l) > 0 else ('(255, 255, 255)', None)
        pixels[x,y] = parseRGB(color)
        print x, y, color

    created.save(open('temp.png', 'w'))

main()
