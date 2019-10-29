from PIL import Image
import random
import pickle

# If you run this change the start and end image numbers and the file path 


def imageDimensions():
    # Create list to hold width, height tuple for each image
    widthList = []          #first element in tuple is WIDTH**
    heightList = []
    lostList = []
    widthSum = 0
    heightSum = 0

    # Starting image number
    imageNum = 0

    # Final image number in the image folder
    finalImageNum = 12759

    while imageNum <= finalImageNum:
        try:
            # opens the image as img
            with Image.open('D://GAN_Gallery/Images/' + str(imageNum) + '.jpg') as img:
                # size returns a tuple (width, height)
                temp_tuple = img.size

                if temp_tuple[0] >= 400 and temp_tuple[1] >= 400:
                    # Put image dimension tuple into list
                    widthList.append(temp_tuple[0])
                    heightList.append(temp_tuple[1])

                    # sum dims
                    widthSum += temp_tuple[0]
                    heightSum += temp_tuple[1]

                else:
                    lostList.append(temp_tuple)

        except:
            print("img not found")
        # Increment the image title
        imageNum += 1


    print("WIDTH:")
    print("avg-")
    print(widthSum / len(widthList))
    print("min-")
    print(min(widthList))
    print("max-")
    print(max(widthList))

    print("HEIGHT:")
    print("avg-")
    print(heightSum / len(heightList))
    print("min-")
    print(min(heightList))
    print("max-")
    print(max(heightList))

    print("MISC:")
    print(len(lostList))
    print(lostList)

def resize():
    # Final image number in the image folder
    finalImageNum = 12762

    for imageNum in range(0, finalImageNum + 1):
        #imageNum = round(random.random() * finalImageNum)

        try:
            # opens the image as img
            with Image.open('D://GAN_Gallery/Images/' + str(imageNum) + '.jpg') as img:
                # size returns a tuple (width, height)
                newImg = img.resize((400, 400))

                with open('D://GAN_Gallery/resize/' + str(imageNum) + '.jpg', 'w') as file:
                    newImg.save(file, "JPEG")
        except:
            continue
        # Increment the image title
        imageNum += 1

# Run the function
#imageDimensions()
resize()
