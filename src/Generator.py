import torch
import torch.nn as nn
import torch.nn.functional as F

"""
    create a class that extends torch.nn.Module. Module is the base class for all neural networks (NNs) in Pytorch
"""
class Generator(nn.Module):
    """
        To extend Module we need to implement both the NN constructor [__init__()] and the forward pass method [forward(Tensor)]
    """
    def __init__(self):
        # call the super constructor
        super(Generator, self).__init__()

        # set up layers as class attributes
        self.linear1 = nn.Linear(125, 256, True)

        self.convTrans1 = nn.ConvTranspose2d(1, 50, 25, 2)        #params(input channels, output channels, kernel size, input padding)
        self.batchNorm1 = nn.BatchNorm2d(50)                       #normalizing the outputs of the first layer

        self.convTrans2 = nn.ConvTranspose2d(50, 10, 55, 2)
        self.batchNorm2 = nn.BatchNorm2d(10)

        self.convTrans3 = nn.ConvTranspose2d(10, 3, 76, 2)
        self.batchNorm3 = nn.BatchNorm2d(3)

        self.ReLU = nn.ReLU()                                   #Rectified Linear Unit to keep our outputs between 0 and 1

    def forward(self, t):
        t = self.linear1(t)
        t = t.reshape(t.size()[0], 1, 16, 16)

        t = self.convTrans1(t)
        t = self.batchNorm1(t)
        t = self.ReLU(t)

        t = self.convTrans2(t)
        t = self.batchNorm2(t)
        t = self.ReLU(t)

        t = self.convTrans3(t)
        t = self.batchNorm3(t)
        t = self.ReLU(t)
        return t


# gen = Generator()
# t = torch.rand(2,1,1,125)
# art = gen(t)
# print(art.size())