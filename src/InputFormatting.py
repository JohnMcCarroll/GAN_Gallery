import torch
import torchvision
import os
from PIL import Image
import pickle


def formatData(data_path):
    dataset = list()
    trans = torchvision.transforms.ToTensor()
    imgs = os.listdir(data_path)
    counter = 0
    partitions = 2
    partition_nums = [int(len(imgs) / 4), int(2 * len(imgs) / 4), int(3 * len(imgs) / 4), len(imgs)]

    for i in range(partitions):
        for img in imgs:
            if counter >= partition_nums[i]:
                break

            img_path = data_path + '/' + img

            try:
                image = Image.open(img_path)
                image = trans(image)

                if image.shape != torch.Size([3, 400, 400]):
                    # vet image sizes
                    continue

                dataset.append(image)
            except Exception as e:
                print(str(e))

            counter += 1

        with open(r'dataset' + str(i) + '.db', 'wb') as file:
            pickle.dump(dataset, file)


formatData("data")
