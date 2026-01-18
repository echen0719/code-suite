# https://colab.research.google.com/drive/1Y0AfQRT_QhK-WmGIr53FcKwduS8Cp5Em
from nnFunctions import *

import torch
from torch import nn
from torch.utils.data import DataLoader

import torchvision
from torchvision import datasets
from torchvision import transforms

import matplotlib.pyplot as plt
import random

device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(42)
torch.cuda.manual_seed(42)

classMappings = []

def dataVisualization(dataLoader):
    figure = plt.figure(figsize=(12, 12))
    images, labels = next(iter(dataLoader))

    for i in range(16):
        index = random.randint(0, len(images) - 1)
        img = images[index]
        label = labels[index].item()
        ax = figure.add_subplot(4, 4, i + 1)
        ax.imshow(img.permute(1, 2, 0)) # CHW -> HWC
        ax.axis('off')
        ax.set_title(classMappings[label])
    plt.show()

class CNNModel(nn.Module):
    def __init__(self, in_features, out_features, hidden_units=32):
        super().__init__()
        # Input shape: (32, 3, 224, 224)
        self.conv_block = nn.Sequential(
            nn.Conv2d(in_channels=in_features, out_channels=hidden_units, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(hidden_units), # normalize data to improve training
            nn.ReLU(),

            nn.Conv2d(in_channels=hidden_units, out_channels=hidden_units, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(hidden_units),
            nn.ReLU(),

            nn.Conv2d(in_channels=hidden_units, out_channels=hidden_units, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            # Ouput shape: (32, 32, 224, 224)

            nn.MaxPool2d(kernel_size=2), # simplfies image by (2x2) or 4 times
            # Output shape: (32, 32, 112, 112)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(), # flattens to 32 x 112 x 112
            nn.Linear(in_features=hidden_units*112*112, out_features=out_features)
        )

    def forward(self, x):
        x = self.conv_block(x)
        x = self.classifier(x)
        return x

def main():
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # according to most websites, this is a pretty common dimension
        transforms.ToTensor()
    ])

    trainData = datasets.Food101(root='data', split="train", download=True, transform=transform)
    testData = datasets.Food101(root='data', split="test", download=True, transform=transform)
    global classMappings; classMappings = trainData.classes # too lazy to use pass as an argument

    trainDataLoader = DataLoader(trainData, batch_size=64, shuffle=True)
    testDataLoader = DataLoader(testData, batch_size=64, shuffle=False)

    ## dataVisualization(trainDataLoader)

    model = CNNModel(3, 101).to(device)
    lossFx = nn.CrossEntropyLoss()
    optim = torch.optim.Adam(params=model.parameters(), lr=1e-4)

    for trial in range(10):
        print("Trial {}: ".format(trial + 1), end='')
        trainStep(model, trainDataLoader, lossFx, optim, accuracy, device)

    testStep(model, testDataLoader, lossFx, optim, accuracy, device)
    torch.save(model.state_dict(), 'model.pth')

if __name__ == '__main__':
    main()