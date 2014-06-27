import urllib2
import json
from bs4 import BeautifulSoup


def get():
    for i in range(2,17):
        res = urllib2.urlopen('http://www.artgalleryartist.com/bob-ross/index' + str(i) + '.htm')
        soup = BeautifulSoup(res)
    
        urls = []
        for img in soup.find_all('img'):
            url = img.get('src')
            if url.startswith('thumbnail'):
                urls.append(url)

        for url in urls:
            img = urllib2.urlopen("http://www.artgalleryartist.com/bob-ross/" + url)
            output = open('img/' + url[11:], 'w')
            output.write(img.read())
            output.close()


get()
