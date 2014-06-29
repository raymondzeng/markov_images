import pickle
import numpy
from collections import Counter
from PIL import Image
import os

def accumulate(dir_path, width, height):
    # acc = numpy.empty([width, height], dtype=list)
    # acc.fill([])
    
    # for x in range(width):
    #     for y in range(height):
    #         acc[x][y] = []

    acc = []
    for _ in range(width):
        l = []
        for _ in range(height):
            l.append([])
        acc.append(l)

    for filename in os.listdir(dir_path):
        if 'test_' not in filename:
            continue

        print filename

        image = Image.open(os.path.join(dir_path, filename))
        pixels = image.load()

        for i in range(0, min(image.size[0], width)):
            for j in range(0, min(image.size[1], height)):
                #temp = list(acc[i][j])
                #temp.append(pixels[i,j])
                #acc[i][j] = temp
                acc[i][j].append(pixels[i,j])
    return acc

# s is in the form '(r, g, b)'
def parseRGB(s):
    vals = s.split()
    return (int(vals[0]), int(vals[1]), int(vals[2]))

def generate(data, output_path, width, height):
    print "starting gen"
    created = Image.new("RGB", (width, height))
    pixels = created.load()

    #for (x,y), value in numpy.ndenumerate(data):
    #if x > width - 1 or y > height - 1:
    #       continue
    
    for x in range(len(data)):
        for y in range(len(data[x])):
            mc = Counter(data[x][y]).most_common(1)
            color, _ = mc[0] if len(mc) > 0 else ((255, 255, 255), None)
            pixels[x,y] = color # parseRGB(color)
            #print x, y, color

    print "writign"
    created.save(open(output_path, 'w'))

def main(images_path, output_path, width, height):
    data = accumulate(images_path, width, height)
    generate(data, output_path, width, height)

land_in = 'img/test/landscape'
port_in = 'img/test/portrait'

lg_land_in = 'img/test/large/landscape'
lg_port_in = 'img/test/large/portrait'

land_out = 'tnland.png'
port_out = 'tnport.png'

lg_land_out = 'land.png'
lg_port_out = 'port.png'

if __name__ == "__main__":
    #main(land_in, land_out, 100, 80)
    #main(port_in, port_out, 80, 100)
    
    #main(lg_land_in, lg_land_out, 900, 680)
    main(lg_port_in, lg_port_out, 680, 900)
