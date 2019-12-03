import torch
import torch.nn as nn
import torch.nn.functional as F

# nn.Module is being extended -- Not a parameter
class Discriminator(nn.Module):

    def __init__(self):
        super(Discriminator, self).__init__()

        # torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1,
        # bias=True, padding_mode='zeros')
        self.conv1 = nn.Conv2d(3, 3, 40, 2)
        self.conv2 = nn.Conv2d(3, 3, 40, 2)
        self.conv3 = nn.Conv2d(3, 3, 30, 2)
        self.conv4 = nn.Conv2d(3, 1, 10, 2)

        self.norm1 = nn.BatchNorm2d(3)
        self.norm2 = nn.BatchNorm2d(3)
        self.norm3 = nn.BatchNorm2d(3)
        self.norm4 = nn.BatchNorm2d(1)

        self.linear = nn.Linear(36,1,True)

        # rectified linear unit
        self.linearUnit = nn.ReLU()


    def forward(self, inputTensor):
        # input is inputTensor
        outputTensor = self.conv1(inputTensor)
        outputTensor = self.norm1(outputTensor)
        #outputTensor = self.linearUnit(outputTensor)

        outputTensor = self.conv2(outputTensor)
        outputTensor = self.norm2(outputTensor)
        #outputTensor = self.linearUnit(outputTensor)

        outputTensor = self.conv3(outputTensor)
        outputTensor = self.norm3(outputTensor)
        #outputTensor = self.linearUnit(outputTensor)

        outputTensor = self.conv4(outputTensor)
        outputTensor = self.norm4(outputTensor)
        #outputTensor = self.linearUnit(outputTensor)

        outputTensor = outputTensor.reshape(outputTensor.size()[0], 1, 1, 36)

        outputTensor = self.linear(outputTensor)

        return outputTensor


# dis = Discriminator()
# input = torch.rand([2, 3, 400, 400])
# output = dis(input)
# print(output.size())
