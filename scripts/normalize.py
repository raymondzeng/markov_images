from PIL import Image
import math
import os

def floor(r, g, b):
  return (int(math.floor(r / 10)) * 10, 
          int(math.floor(g / 10)) * 10, 
          int(math.floor(b / 10)) * 10)


def pixelate(pixelSize, image):
  image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize), Image.NEAREST)
  image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)

  return image

# changes in place
def normalizeImage(image):
  pixels = image.load()

  for i in range(0,image.size[0]):
    for j in range(0,image.size[1]):
      r, g, b = pixels[i, j] 
      pixels[i, j] = floor(r, g, b)

def normalizeAll(dir_path, output_path):
  for filename in os.listdir(dir_path):
    if 'test_' in filename:
      continue
    print filename
    image = Image.open(os.path.join(dir_path, filename))
    normalizeImage(image)
    image.save(os.path.join(output_path, 'test_' + filename.replace('.jpg', '.png')))

land_in = 'img/tn/landscape'
port_in = 'img/tn/portrait'

land_out = 'img/test/landscape/'
port_out = 'img/test/portrait/'

lg_land_in = 'img/large/landscape'
lg_port_in = 'img/large/portrait'

lg_land_out = 'img/test/large/landscape/'
lg_port_out = 'img/test/large/portrait/'

if __name__ == "__main__":
  #normalizeAll(land_in, land_out)
  #normalizeAll(port_in, port_out)
  normalizeAll(lg_land_in, lg_land_out)
  normalizeAll(lg_port_in, lg_port_out)

    
