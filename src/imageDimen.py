from PIL import Image

def imageDimensions():
    # Create list to hold width, height tuple for each image
    dimensionList = []

    # Starting image number
    imageNum = 2881

    # Final image number in the image folder
    finalImageNum = 2890

    while imageNum <= finalImageNum:
        # opens the image as img
        with Image.open('C:/Users/Troy/PycharmProjects/GAN_Gallery/Images/' + str(imageNum) + '.jpg') as img:
            # size returns a tuple (width, height)
            temp_tuple = img.size
            # Put image dimension tuple into list
            dimensionList.append(temp_tuple)
        # Increment the image title
        imageNum += 1


    print(dimensionList)
    print("Total images: " + str(len(dimensionList)))


# Run the function
imageDimensions()
