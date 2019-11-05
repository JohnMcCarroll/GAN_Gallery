import torch
import torch.nn as nn
import torch.nn.functional as F

# nn.Module is being extended -- Not a parameter
class Discriminator(nn.Module):

    def __init__(self):
        super(Discriminator, self).__init__()

        # torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1,
        # bias=True, padding_mode='zeros')
        self.conv1 = nn.Conv2d(3, 3, 4, 1)
        self.conv2 = nn.Conv2d(3, 3, 2, 1, 2)
        #self.conv3 = nn.Conv2d(3, 3, 1, 1)

        # rectified linear unit
        self.linearUnit = nn.ReLU()


    def forward(self, inputTensor):
        # input is t
        outputTensor = self.conv1(inputTensor)
        # fix any values to make sure they are between 0 and 1
        outputTensor = self.linearUnit(outputTensor)
        outputTensor = self.conv2(outputTensor)
        # fix any values to make sure they are between 0 and 1
        #outputTensor = self.linearUnit(outputTensor)
        #outputTensor = self.conv3(outputTensor)


        # fix any values to make sure they are between 0 and 1
        outputLinearUnit = self.linearUnit(outputTensor)

        return outputLinearUnit


dis = Discriminator()
input = torch.zeros([1, 3, 400, 400])
output = dis(input)
print(output.size())
