# check this out: https://www.learnpytorch.io/03_pytorch_computer_vision/

import torch
from torch import nn
import torchvision
from torchvision import datasets
from torchvision import transforms
# transforms.ToTensor
import matplotlib.pyplot as plt

trainData = datasets.CIFAR10(root="data", train=True, download=True, transform=transforms.ToTensor(), target_transform=None)
testData = datasets.CIFAR10(root="data", train=False, download=True, transform=transforms.ToTensor())
# shape of each tensor is [3, 32, 32]

## print(trainData.classes) # out: ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']