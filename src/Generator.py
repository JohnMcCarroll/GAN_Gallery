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
        self.linear1 = nn.Linear(125, 1024, True)

        self.convTrans1 = nn.ConvTranspose2d(1, 50, 19)
        self.batchNorm1 = nn.BatchNorm2d(50)

        self.convTrans2 = nn.ConvTranspose2d(50, 40, 2, 2)        #params(input channels, output channels, kernel size, input padding)
        self.batchNorm2 = nn.BatchNorm2d(40)                       #normalizing the outputs of the first layer

        self.convTrans3 = nn.ConvTranspose2d(40, 30, 2, 2)
        self.batchNorm3 = nn.BatchNorm2d(30)

        self.convTrans4 = nn.ConvTranspose2d(30, 20, 2, 2)
        self.batchNorm4 = nn.BatchNorm2d(20)

        self.convTrans5 = nn.ConvTranspose2d(20, 3, 1)
        self.batchNorm5 = nn.BatchNorm2d(3)

        self.ReLU = nn.ReLU()                                   #Rectified Linear Unit to keep our outputs between 0 and 1

    def forward(self, t):
        t = self.linear1(t)
        t = t.reshape(t.size()[0], 1, 32, 32)

        t = self.convTrans1(t)
        t = self.batchNorm1(t)
        #t = self.ReLU(t)

        t = self.convTrans2(t)
        t = self.batchNorm2(t)
        #t = self.ReLU(t)

        t = self.convTrans3(t)
        t = self.batchNorm3(t)
        #t = self.ReLU(t)

        t = self.convTrans4(t)
        t = self.batchNorm4(t)
        #t = self.ReLU(t)

        t = self.convTrans5(t)
        t = self.batchNorm5(t)
        #t = self.ReLU(t)

        return t


# gen = Generator().cuda()
# t = torch.rand(2,1,1,125).cuda()
# art = gen(t)
# print(art.size())