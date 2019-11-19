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



with open(r'D:\GAN_Gallery\src\dataset1a.db', 'rb') as file:                # Break down db files into smaller chunks if RAM issue persists
    #pickle.dump(dataset, file)
    dataset1 = pickle.load(file)

# with open(r'D:\GAN_Gallery\src\dataset2.db', 'rb') as file:
#     #pickle.dump(dataset, file)
#     dataset2 = pickle.load(file)

index = 0
for datum in dataset1:
    if datum.size() != torch.Size([3, 400, 400]):
        dataset1.pop(index)
    index += 1

with open(r'D:\GAN_Gallery\src\dataset1a.db', 'wb') as file:
    pickle.dump(dataset1, file)

with open(r'D:\GAN_Gallery\src\smallData.db', 'wb') as file:
    pickle.dump(dataset1[0:101], file)
