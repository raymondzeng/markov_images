from PIL import Image
import os
from collections import Counter
import numpy
import pickle

def accumulate(dir_path, output_path, width, height):
    acc = numpy.empty([width, height], dtype=list)
    acc.fill([])

    for filename in os.listdir(dir_path):
        if 'test_' not in filename:
            continue

        print filename

        image = Image.open(os.path.join(dir_path, filename))
        pixels = image.load()

        for i in range(0, min(image.size[0], width)):
            for j in range(0, min(image.size[1], height)):
                color = str(pixels[i,j])
                temp = list(acc[i][j])
                temp.append(color)
                acc[i][j] = temp

    #pickle.dump(acc, open(output_path, 'wb'))
    numpy.save(output_path, acc)

land_in = 'img/test/landscape'
port_in = 'img/test/portrait'

land_out = 'acc_data/tnland.npy'
port_out = 'acc_data/tnport.npy'

lg_land_in = 'img/test/large/landscape'
lg_port_in = 'img/test/large/portrait'

lg_land_out = 'acc_data/land.npy'
lg_port_out = 'acc_data/port.npy'

if __name__ == "__main__":
    #accumulate(land_in, land_out, 100, 80)
    #accumulate(port_in, port_out, 80, 100)

    #accumulate(lg_land_in, lg_land_out, 900, 680)
    accumulate(lg_port_in, lg_port_out, 680, 900)
