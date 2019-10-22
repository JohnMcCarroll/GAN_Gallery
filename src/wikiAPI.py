
import urllib.request
import requests
import time
import pickle

##Parse JSON file and get art url and title
## Save url to picURL
## Save title to pic title

##Url of picture
from sphinx.util import requests

# attributes
artistIDs = set()
imageURLs = set()

picURL = 'https://uploads1.wikiart.org/images/gerhard-richter/abstract-painting-780-1.jpg!Large.jpg'
# Folder to save image to
picPath = 'images/'
# Title of Picture
picTitle = 'Abstract'


def getImage(picURL, picPath, picTitle):
    finalPath = picPath + picTitle + '.jpg'
    # image = urllib.URLopener()
    urllib.request.urlretrieve(picURL, finalPath)

def getArtists():
    # get list of artists by genre / medium and store in set
    artistsURL = "https://www.wikiart.org/en/api/2/UpdatedArtists"
    paginatedURL = ""
    hasMore = True
    paginationToken = ""
    while hasMore:
        # get page of list of artists
        request = requests.get(artistsURL + paginatedURL).text

        # update hasMore
        request = request.split("\"hasMore\":")

        # break if end of list
        if len(request) < 2:
            break

        # Checking hasMore in split string for true or false
        if request[1] == "true}":
            hasMore = True
        else:
            hasMore = False

        # update pagination token
        request = request[0].split("\"paginationToken\":")
        paginationToken = request[1].strip("\",")

        #print(request)
        #print(paginationToken)


        # update URL
        paginatedURL = "?paginationToken=" + paginationToken

        # add to set of artists
        request = request[0].split("\"artistName\":")
        for artist in request:
            if artist[-2] == "]":
                continue
            id = artist[-26:-2]
            artistIDs.add(id)

        time.sleep(10)

# populates imageURLs set with painting URLs
def getPaintingURLs():
    # Main url
    listURL = "https://www.wikiart.org/en/api/2/PaintingsByArtist?id="
    paginatedURL = ""
    # Set hasMore default to true
    hasMore = True
    # Set default token to empty string
    paginationToken = ""
    for id in artistIDs:
        while hasMore:
            # get page of list of artists
            request = requests.get(listURL + id + paginatedURL).text

            # update hasMore
            request = request.split("\"hasMore\":")

            # break if end of list
            if len(request) < 2:
                break

            if request[1] == "true}":
                hasMore = True
            else:
                hasMore = False

            # update pagination token
            request = request[0].split("\"paginationToken\":")
            paginationToken = request[1].strip("\",")

            # update URL component
            paginatedURL = "&paginationToken=" + paginationToken

            # add to set of URLs
            request = request[0].split("\"height\":")
            for url in request:

                url = url.split("\"image\":")

                if len(url) > 1:
                    image = url[1].strip("\",")
                    print(image)
                    imageURLs.add(image)

            time.sleep(10)

        # reset hasMore
        hasMore = True


            # get Image URL - "image":"https://uploads.wikiart.org/Content/images/ARTIST-480x600.jpg","wikipediaUrl":
            # This should split a string twice to single out the image url
            # imageSplit = request.split('\"image\":\"')
            # linkSplit = imageSplit.split('\",\"wikipediaUrl\"')

            # imageURLs.add(linkSplit[0])

            # loop through imageUrls and download each image using function above




getArtists()
getPaintingURLs()


# list of mediums to include:
# - canvas
# - acrylic
# - brush?