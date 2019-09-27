
import urllib.request

##Parse JSON file and get art url and title
## Save url to picURL
## Save title to pic title

##Url of picture
from sphinx.util import requests

picURL = 'https://uploads1.wikiart.org/images/gerhard-richter/abstract-painting-780-1.jpg!Large.jpg'
##Folder to save image to
picPath = 'images/'
##Title of Picture
picTitle = 'Abstract'

def getImage(picURL, picPath, picTitle):
    finalPath = picPath + picTitle + '.jpg'
    ##image = urllib.URLopener()
    urllib.request.urlretrieve(picURL, finalPath)


getImage(picURL, picPath, picTitle)

