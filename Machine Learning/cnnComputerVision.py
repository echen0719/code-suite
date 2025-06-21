# check this out: https://www.learnpytorch.io/03_pytorch_computer_vision/
# refer to nnComputerVision for extended clarification

import torch
from torch import nn
from torch.utils.data import DataLoader
import torchvision
from torchvision import datasets
from torchvision import transforms
from torchvision.datasets import ImageFolder
from nnFunctions import *

device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(42)
torch.cuda.manual_seed(42)
torch.set_num_threads(4)

# https://poloclub.github.io/cnn-explainer/
class CIFARModel(nn.Module):
    def __init__(self, in_features, out_features, hidden_units=10):
        super().__init__()
        self.conv_block1 = nn.Sequential(
            # kernel_size determines how many pixels to look at once
            # moves over one pixel at a time with stride 1
            # padding adds pixels so model can understand edges
            nn.Conv2d(in_channels=in_features, out_channels=hidden_units, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=hidden_units, out_channels=hidden_units, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2) # 2x2 square moves over image, reducing shape to half size
        )
        self.conv_block2 = nn.Sequential(
            nn.Conv2d(in_channels=hidden_units, out_channels=hidden_units, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=hidden_units, out_channels=hidden_units, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.classifier = nn.Sequential(
                nn.Flatten(), # because of nn.Flatten()
                # in_feautures = hidden_units * (final size after maxpools/2*2)^2
                nn.Linear(in_features=hidden_units * 64, out_features=out_features)
        )

    def forward(self, x):
        x = self.conv_block1(x)
        x = self.conv_block2(x)
        ## print("Shape before classifier: {}".format(x.shape))
        x = self.classifier(x)
        return x

# Uncomment for CINIC-10 images to prevent overfitting
trainData = ImageFolder(root="data/cinic-10-py/train", transform=transforms.ToTensor(), target_transform=None)
testData = ImageFolder(root="data/cinic-10-py/test", transform=transforms.ToTensor())

# trainData = datasets.CIFAR10(root="data", train=True, download=True, transform=transforms.ToTensor(), target_transform=None)
# testData = datasets.CIFAR10(root="data", train=False, download=True, transform=transforms.ToTensor())

classesLength = len(trainData.classes)

trainDataLoader = DataLoader(dataset=trainData, batch_size=64, shuffle=True)
testDataLoader = DataLoader(dataset=testData, batch_size=64)

def accuracy(yPreds, yTrue):
    correct = torch.eq(yTrue, yPreds).sum().item()
    return correct / len(yPreds)

# in_features is color channels
model = CIFARModel(in_features=3, out_features=classesLength).to(device)
## print(model(trainData[0][0].unsqueeze(0).to(device))) # size is [1, 10]

lossFx = nn.CrossEntropyLoss()
optim = torch.optim.SGD(params=model.parameters(), lr=0.01)

for trial in range(5):
    print("Trial {}: ".format(trial + 1), end='')
    trainStep(model, trainDataLoader, lossFx, optim, accuracy, device)
    testStep(model, testDataLoader, lossFx, optim, accuracy, device)

'''
Trial 1: TrLoss: 2.302616 | TrAcc: 0.103441 | TeLoss: 2.302126 | TeAcc: 0.100020
Trial 2: TrLoss: 2.300431 | TrAcc: 0.116848 | TeLoss: 2.294677 | TeAcc: 0.121616
Trial 3: TrLoss: 2.205950 | TrAcc: 0.185362 | TeLoss: 2.154494 | TeAcc: 0.197054
Trial 4: TrLoss: 2.064754 | TrAcc: 0.266884 | TeLoss: 2.080848 | TeAcc: 0.245721
Trial 5: TrLoss: 1.925956 | TrAcc: 0.314678 | TeLoss: 1.880924 | TeAcc: 0.324144
'''