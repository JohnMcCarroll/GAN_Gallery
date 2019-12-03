import torch
import torchvision
import os
from PIL import Image
import pickle

def formatData():
    rootPath = r'D:\GAN_Gallery\resize'
    dataset = list()
    trans = torchvision.transforms.ToTensor()
    counter = 0

    for img in os.listdir(rootPath):
        counter += 1
        if counter < 8600:
            continue

        try:
            image = Image.open(rootPath + '\\' + img)
            image = trans(image)
            dataset.append(image)
        except Exception as e:
            print(str(e))

    with open(r'D:\GAN_Gallery\src\dataset3.db', 'wb') as file:
        pickle.dump(dataset, file)


for i in range(3):

    # load in data
    if i % 3 == 0:
        with open(r'D:\GAN_Gallery\src\dataset1a.db', 'rb') as file:
            dataset = pickle.load(file)
    elif i % 3 == 1:
        with open(r'D:\GAN_Gallery\src\dataset2a.db', 'rb') as file:
            dataset = pickle.load(file)
    else:
        with open(r'D:\GAN_Gallery\src\dataset3a.db', 'rb') as file:
            dataset = pickle.load(file)

    # # reduce size
    # index = 0
    # for datum in dataset:
    #     if datum.size() != torch.Size([3, 400, 400]):
    #         dataset.pop(index)
    #     index += 1

    # save data
    if i % 3 == 0:
        with open(r'D:\GAN_Gallery\src\dataset1b.db', 'wb') as file:
            pickle.dump(dataset[0:2001], file)
        with open(r'D:\GAN_Gallery\src\dataset2b.db', 'wb') as file:
            pickle.dump(dataset[2001:len(dataset)], file)
    elif i % 3 == 1:
        with open(r'D:\GAN_Gallery\src\dataset3b.db', 'wb') as file:
            pickle.dump(dataset[0:2001], file)
        with open(r'D:\GAN_Gallery\src\dataset4b.db', 'wb') as file:
            pickle.dump(dataset[2001:len(dataset)], file)
    else:
        with open(r'D:\GAN_Gallery\src\dataset5b.db', 'wb') as file:
            pickle.dump(dataset[0:2001], file)
        with open(r'D:\GAN_Gallery\src\dataset6b.db', 'wb') as file:
            pickle.dump(dataset[2001:len(dataset)], file)
