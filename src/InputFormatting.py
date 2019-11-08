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



with open(r'D:\GAN_Gallery\src\dataset1.db', 'rb') as file:
    #pickle.dump(dataset, file)
    dataset1 = pickle.load(file)

with open(r'D:\GAN_Gallery\src\dataset2.db', 'rb') as file:
    #pickle.dump(dataset, file)
    dataset2 = pickle.load(file)

dataset = dataset1 + dataset2

with open(r'D:\GAN_Gallery\src\dataset.db', 'wb') as file:
    pickle.dump(dataset, file)


print(len(dataset))
print("size:")
print(dataset[0].size())
print("sample:")
print(dataset[0])
