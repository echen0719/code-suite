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
from nnFunctions import *

device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(42)
torch.cuda.manual_seed(42)

class CIFARModel(nn.Module):
    def __init__(self, in_features, out_features, hidden_units=8):
        super().__init__()
        self.linearStack = nn.Sequential(
            nn.Flatten(), # converts to one vector with all data
            nn.Linear(in_features=in_features, out_features=hidden_units),
            nn.ReLU(), # non-linear layer connecting linear layers
            nn.Linear(in_features=hidden_units, out_features=hidden_units),
            nn.ReLU(),
            nn.Linear(in_features=hidden_units, out_features=out_features),
            nn.ReLU()
        )
    def forward(self, x):
        return self.linearStack(x)

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

classesLength = len(trainData.classes) # this multiclass dataset has 10 classes (CIFAR10)
## print(trainData.classes) # out: ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
## print(trainData.class_to_idx); print(trainData[0][1]) # out: 6 which is frog
## visualization(trainData)

# using DataLoader to split data into batches of 32 which creates computational advantages
trainDataLoader = DataLoader(dataset=trainData, batch_size=64, shuffle=True) # 782 batches
testDataLoader = DataLoader(dataset=testData, batch_size=64) # 157 batches

# trainFeaturesBatch, trainLabelsBatch = next(iter(trainDataLoader))
# testFeaturesBatch, testLabelsBatch = next(iter(testDataLoader))

## visualization(trainDataLoader) # visualizes 9 images from a random train data batch

# 3 color channels * 32px * 32px = 3072 features
model = CIFARModel(in_features=3072, out_features=classesLength).to(device)

# copied from previous
def accuracy(yPreds, yTrue):
    correct = torch.eq(yTrue, yPreds).sum().item()
    return correct / len(yPreds)

lossFx = nn.CrossEntropyLoss()
optim = torch.optim.Adam(params=model.parameters(), lr=0.001)

for trial in range(5):
    accuTrLoss, accuTrAcc = 0, 0
    model.train()
    # one batch of data goes through inner training loop
    for batch, (image, label) in enumerate(trainDataLoader):
        image, label = image.to(device), label.to(device)
        trLogits = model(image)
        trLoss = lossFx(trLogits, label)
        accuTrLoss += trLoss
        accuTrAcc += accuracy(trLogits.argmax(dim=1), label)
        optim.zero_grad()
        trLoss.backward()
        optim.step()
        # model optimizes itself after each batch
    accuTrLoss /= len(trainDataLoader) # gets trLoss average for each batch
    accuTrAcc /= len(trainDataLoader) # gets trAcc average for each batch

    accuTeLoss, accuTeAcc = 0, 0
    model.eval()
    with torch.inference_mode():
        for batch, (image, label) in enumerate(testDataLoader):
            image, label = image.to(device), label.to(device)
            teLogits = model(image)
            accuTeLoss += lossFx(teLogits, label)
            accuTeAcc += accuracy(teLogits.argmax(dim=1), label)
        accuTeLoss /= len(testDataLoader) # gets teLoss average for each batch
        accuTeAcc /= len(testDataLoader) # gets teAcc average for each batch

    print("Trial {}: TrLoss: {:3f} | TrAcc: {:3f} | TeLoss: {:3f} | TeAcc: {:3f}".format(trial + 1, accuTrLoss, accuTrAcc, accuTeLoss, accuTeAcc))

for trial in range(5):
    print("Trial {}: ".format(trial + 1), end='')
    trainStep(model, trainDataLoader, lossFx, optim, accuracy, device)
    testStep(model, testDataLoader, lossFx, optim, accuracy, device)