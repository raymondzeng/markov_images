from PIL import Image
import math
import os

dir = "test_landscape"

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

if __name__ == "__main__":
  for filename in os.listdir(dir):
    if 'test_' in filename:
      pass
    image = Image.open(os.path.join(dir, filename))
    image = Image.open('temp.png')  
    #  image = pixelate(4, image)
    normalizeImage(image)
    image.save(os.path.join(dir, 'test_' + filename.replace('.jpg', '.png')))
    
