# check this out: https://www.learnpytorch.io/03_pytorch_computer_vision/
import torch
from torch import nn
from torch.utils.data import DataLoader
import torchvision
from torchvision import datasets
from torchvision import transforms
# transforms.ToTensor
import matplotlib.pyplot as plt
import random

# use matplotlib to represent tensors as visuals
def visualization(data):
    images = next(iter(data))[0]
    figure = plt.figure(figsize=(9, 9))
    for i in range(9): # displays 9 different random images
        index = random.randint(0, len(images) - 1)
        img = images[index].permute(1, 2, 0) # change [3, 32, 32] -> [32, 32, 3]
        figure.add_subplot(3, 3, i + 1)
        plt.imshow(img) # haven't worked with matplotlib figures yet
        plt.axis('off')
    plt.show()

trainData = datasets.CIFAR10(root="data", train=True, download=True, transform=transforms.ToTensor(), target_transform=None)
testData = datasets.CIFAR10(root="data", train=False, download=True, transform=transforms.ToTensor())
# shape of each tensor is [3, 32, 32]

## print(trainData.classes) # out: ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
## print(trainData.class_to_idx); print(trainData[0][1]) # out: 6 which is frog
## visualization(trainData)

# using DataLoader to split data into batches of 32 which creates computational advantages
trainDataLoader = DataLoader(dataset=trainData, batch_size=32, shuffle=True) # 1563 batches
testDataLoader = DataLoader(dataset=testData, batch_size=32) # 313 batches

## visualization(trainDataLoader) # visualizes 9 images from a random train data batch