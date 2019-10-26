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
        self.convTrans1 = nn.ConvTranspose2d(125, 100, 4, 2)        #params(input channels, output channels, kernel size, input padding)
        self.batchNorm1 = nn.BatchNorm2d(100)                       #normalizing the outputs of the first layer

        self.convTrans2 = nn.ConvTranspose2d(100, 80, 4, 2)
        self.batchNorm2 = nn.BatchNorm2d(80)

        self.convTrans3 = nn.ConvTranspose2d(80, 50, 8, 2)
        self.batchNorm3 = nn.BatchNorm2d(50)

        self.convTrans4 = nn.ConvTranspose2d(50, 30, 6, 2)
        self.batchNorm4 = nn.BatchNorm2d(30)

        self.convTrans5 = nn.ConvTranspose2d(30, 10, 10, 2)
        self.batchNorm5 = nn.BatchNorm2d(10)

        self.convTrans6 = nn.ConvTranspose2d(10, 5, 8, 2)
        self.batchNorm6 = nn.BatchNorm2d(5)

        self.convTrans7 = nn.ConvTranspose2d(5, 3, 10, 2)
        self.batchNorm7 = nn.BatchNorm2d(3)

        self.ReLU = nn.ReLU()                                   #Rectified Linear Unit to keep our outputs between 0 and 1

    def forward(self, t):
        t = self.convTrans1(t)
        t = self.batchNorm1(t)
        t = self.ReLU(t)

        t = self.convTrans2(t)
        t = self.batchNorm2(t)
        t = self.ReLU(t)

        t = self.convTrans3(t)
        t = self.batchNorm3(t)
        t = self.ReLU(t)

        t = self.convTrans4(t)
        t = self.batchNorm4(t)
        t = self.ReLU(t)

        t = self.convTrans5(t)
        t = self.batchNorm5(t)
        t = self.ReLU(t)

        t = self.convTrans6(t)
        t = self.batchNorm6(t)
        t = self.ReLU(t)

        t = self.convTrans7(t)
        t = self.batchNorm7(t)
        t = self.ReLU(t)

        return t

gen = Generator()
t = torch.Tensor(1,125,1,1)
art = gen(t)
print(art.size())