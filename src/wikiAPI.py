import urllib.request
import requests
import time
import pickle
from sphinx.util import requests

# attributes
artistIDs = set()
imageURLs = set()
progress = 0

picURL = 'https://uploads1.wikiart.org/images/gerhard-richter/abstract-painting-780-1.jpg!Large.jpg'
# Folder to save image to
picPath = 'images/'
# Title of Picture
picTitle = 'Abstract'


def getImage(picURL, picPath, picTitle):
    finalPath = picPath + picTitle + '.jpg'
    # image = urllib.URLopener()
    try:
        urllib.request.urlretrieve(picURL, finalPath)
    except:
        print("the one that got away: " + picURL)


def getArtists():
    progress = 0
    # get list of artists by genre / medium and store in set
    artistsURL = "https://www.wikiart.org/en/api/2/UpdatedArtists"
    paginatedURL = ""
    hasMore = True
    paginationToken = ""
    while hasMore and progress < 10:          #TODO: remove***
        print(progress)
        progress += 1

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


# populates imageURLs set with painting URLs
def getPaintingURLs():
    progress = 0
    # Main url
    listURL = "https://www.wikiart.org/en/api/2/PaintingsByArtist?id="
    paginatedURL = ""
    # Set hasMore default to true
    hasMore = True
    # Set default token to empty string
    paginationToken = ""
    for id in artistIDs:
        while hasMore and progress < 10:     # TODO: remove**
            print(progress)
            progress += 1

            try:
                # get page of list of artists
                request = requests.get(listURL + id + paginatedURL).text
            except:
                continue

            # update hasMore
            request = request.split("\"hasMore\":")

            # break if end of list
            if len(request) < 2:
                break

            if request[1] == "true}":
                hasMore = True

                # update pagination token
                request = request[0].split("\"paginationToken\":")
                paginationToken = request[1].strip("\",")

                # update URL component
                paginatedURL = "&paginationToken=" + paginationToken
            else:
                hasMore = False

                # reset paginatedURL if next request is new artist (aka no pagination token on first page)
                paginatedURL = ""


            # add to set of URLs
            request = request[0].split("\"height\":")
            for url in request:

                url = url.split("\"image\":")

                if len(url) > 1:
                    image = url[1].strip("\",")
                    print(image)
                    imageURLs.add(image)

        # reset hasMore
        hasMore = True


def downloadImages():
    path = "images/"
    title = 0
    for url in imageURLs:
        getImage(url, path, str(title))
        title += 1


# run the script

getArtists()

try:
   with open(r'artists.pkl', 'wb') as file:
       pickle.dump(artistIDs, file)
except:
   print("oof artist ids")

getPaintingURLs()
try:
    with open(r'image_urls.pkl', 'wb') as file:
        pickle.dump(imageURLs, file)
        #imageURLs = pickle.load(file)
except:
    print("oof image URLs")

downloadImages()


## Parse JSON file and get art url and title
## Save url to picURL
## Save title to pic title
## Url of picture
