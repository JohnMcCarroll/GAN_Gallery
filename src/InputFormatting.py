import torch
import torchvision
import os
from PIL import Image
import pickle

rootPath = r'D:\GAN_Gallery\resize'
dataset = list()


for img in os.listdir(rootPath):
    try:
        image = Image.open(rootPath + '\\' + img)
        #image = torchvision.transforms.ToPILImage(image)
        trans = torchvision.transforms.ToTensor()
        image = trans(image)
        dataset.append(image)
    except:
        print('img doesnt exist')
        continue

with open(r'D:\GAN_Gallery\src\dataset', 'wb') as file:
    pickle.dump(dataset, file)

print(len(dataset))
print(dataset[0].size())