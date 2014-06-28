import urllib2
import os

dir1 = 'img/landscape'
dir2 = 'img/portrait'

out1 = 'img/large/landscape/'
out2 = 'img/large/portrait/'

def get():
    for filename in os.listdir(dir1):
        print filename
        img = urllib2.urlopen('http://www.artgalleryartist.com/bob-ross/images/' + filename[2:])
        output = open(out1 + filename[2:], 'w')
        output.write(img.read())
        output.close()

    for filename in os.listdir(dir2):
        print filename
        img = urllib2.urlopen('http://www.artgalleryartist.com/bob-ross/images/' + filename[2:])
        output = open(out2 + filename[2:], 'w')
        output.write(img.read())
        output.close()

get()
