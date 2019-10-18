
import urllib.request
import requests
import time

##Parse JSON file and get art url and title
## Save url to picURL
## Save title to pic title

##Url of picture
from sphinx.util import requests

# attributes
artistIDs = set()
imageURLs = set()

picURL = 'https://uploads1.wikiart.org/images/gerhard-richter/abstract-painting-780-1.jpg!Large.jpg'
##Folder to save image to
picPath = 'images/'
##Title of Picture
picTitle = 'Abstract'


def getImage(picURL, picPath, picTitle):
    finalPath = picPath + picTitle + '.jpg'
    ##image = urllib.URLopener()
    urllib.request.urlretrieve(picURL, finalPath)

def getArtists():
    ## get list of artists by genre / medium and store in set
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

        if request[1] == "true}":
            hasMore = True
        else:
            hasMore = False

        # update pagination token
        request = request[0].split("\"paginationToken\":")
        paginationToken = request[1].strip("\",")
        print(paginationToken)

        # update URL
        paginatedURL = "?paginationToken=" + paginationToken

        # add to set of artists
        request = request[0].split("\"artistName\":")
        for artist in request:
            if artist[-2] == "]":
                continue
            id = artist[-26:-2]
            artistIDs.add(id)

        #time.sleep(10)

    def getPaintingURLs():
        listURL = "https://www.wikiart.org/en/api/2/PaintingsByArtist?id="



    ## use pagination token to get each new page and use hasMore boolean to know when to move on

    ## iterate through set using artist IDs to get list of painting IDs
    ## use pagination token to get each new page and use hasMore boolean to know when to move on

    ## download each painting in painting ID set in intervals of 10 seconds?


getArtists()
print(artistIDs)


# list of mediums to include:
# - canvas
# - acrylic
# - brush?