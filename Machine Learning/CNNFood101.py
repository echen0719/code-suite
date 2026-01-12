# https://colab.research.google.com/drive/1Y0AfQRT_QhK-WmGIr53FcKwduS8Cp5Em

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
    def __init__(self, out_features=101):
        super().__init__()
        self.stack = nn.Sequential(
            # input is (32, 3, 224, 224)
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True), # according to docs, this doesn't make a copy

            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2), # simplfies image by (2x2) or 4 times

            nn.Flatten()
        )
    def forward(self, x):
        return self.stack(x)

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

    # dataVisualization(trainDataLoader)

    model = CNNModel().to(device)

    model.eval()
    images, labels = next(iter(trainDataLoader))
    index = random.randint(0, len(images) - 1)
    img = images[index].unsqueeze(0)
    print(model(img))

if __name__ == '__main__':
    main()