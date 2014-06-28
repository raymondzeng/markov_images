import pickle
import numpy
from collections import Counter
from PIL import Image

# s is in the form '(r, g, b)'
def parseRGB(s):
    s = s.replace('(', '').replace(')', '').replace(',', '')
    vals = s.split()
    return (int(vals[0]), int(vals[1]), int(vals[2]))

def generate(acc_p, output_path, width, height):
    data = numpy.load(acc_p)
    created = Image.new("RGB", (width, height))
    pixels = created.load()

    for (x,y), value in numpy.ndenumerate(data):
        if x > width - 1 or y > height - 1:
            continue
        l = Counter(value).most_common(1)
        color, _ = l[0] if len(l) > 0 else ('(255, 255, 255)', None)
        pixels[x,y] = parseRGB(color)
        print x, y, color

    created.save(open(output_path, 'w'))

land_in = 'acc_data/tnland.npy'
port_in = 'acc_data/tnport.npy'

land_out = 'tnland.png'
port_out = 'tnport.png'

lg_land_in = 'acc_data/land.npy'
lg_port_in = 'acc_data/port.npy'

lg_land_out = 'land.png'
lg_port_out = 'port.png'

if __name__ == "__main__":
    #generate(land_in, land_out, 100, 80)
    #generate(port_in, port_out, 80, 100)
    #generate(lg_land_in, lg_land_out, 900, 680)
    generate(lg_port_in, lg_port_out, 680, 900)
