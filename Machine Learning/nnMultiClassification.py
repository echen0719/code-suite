# check this out: https://www.learnpytorch.io/02_pytorch_classification/
# refer to nnBinaryClassification for extended clarification

import torch
import torch.nn as nn
import numpy as np
import polars as pol # faster than pandas
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(42)
torch.cuda.manual_seed(42)

class blobModel(nn.Module):
    def __init__(self, in_features, out_features, hidden_units=8): # all ints
        super().__init__()
        self.linearStack = nn.Sequential(
            nn.Linear(in_features=in_features, out_features=hidden_units),
            nn.ReLU(),
            nn.Linear(in_features=hidden_units, out_features=hidden_units),
            nn.ReLU(),
            nn.Linear(in_features=hidden_units, out_features=out_features)
        )
    def forward(self, x):
        return self.linearStack(x)

# similar to two features and 4 labels, cluster_std is size of blobs
xBlob, yBlob = make_blobs(n_samples=1000, n_features=2, centers=4, cluster_std=1.5, random_state=42)
## plt.scatter(xBlob[:, 0], xBlob[:, 1], c=yBlob, cmap=plt.cm.winter)
## plt.show() # to visualize these four blobs

xTensor = torch.from_numpy(xBlob).type(torch.float)
yTensor = torch.from_numpy(yBlob).type(torch.LongTensor) # CEL needs yBlob tensor using int64
xTrain, xTest, yTrain, yTest = train_test_split(xTensor, yTensor, test_size=0.2, random_state=42)

xTrain, yTrain = xTrain.to(device), yTrain.to(device)
xTest, yTest = xTest.to(device), yTest.to(device)

# in_features = n_features, out_features = centers (labels)
model = blobModel(in_features=2, out_features=4).to(device)
## print(model) # print model stack info

def accuracy(yPreds, yTrue): # if needed
    correct = torch.eq(yTrue, yPreds).sum().item() # returns number of yTrue == yPreds
    return correct / len(yPreds)

lossFx = nn.CrossEntropyLoss()
optim = torch.optim.SGD(params=model.parameters(), lr=0.1)

for trial in range(1000):
    model.train()
    trLogits = model(xTrain) # no squeeze needed here
    # trPredProbs is just torch.softmax(trLogits, dim=1)
    trPredLabels = torch.softmax(trLogits, dim=1).argmax(dim=1)
    # dim=1 is left to right with logit size as (800, 4)
    trLoss = lossFx(trLogits, yTrain)
    trAcc = accuracy(trPredLabels, yTrain)
    optim.zero_grad()
    trLoss.backward()
    optim.step()

    model.eval()
    with torch.inference_mode():
        teLogits = model(xTest)
        tePredLabels = torch.softmax(teLogits, dim=1).argmax(dim=1)
        teLoss = lossFx(teLogits, yTest) # same here
        teAcc = accuracy(tePredLabels, yTest)

    if trial % 100 == 0:
        print("Trial: {} | TrLoss: {:.3f} | TeLoss: {:.3f} | TrAcc: {:.3f} | TeACC: {:.3f}".format(trial, trLoss, teLoss, trAcc, teAcc))