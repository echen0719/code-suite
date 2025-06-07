# check this out: https://www.learnpytorch.io/02_pytorch_classification/

import torch
import torch.nn as nn
import numpy as np
import polars as pol # faster than pandas
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(42)
torch.cuda.manual_seed(42)

class circleModel(nn.Module):
    def __init__(self):
        super().__init__()
        # xTrain size is (800, 2) so in = 2
        # yTrain size is (800) so out = 1

        # self.layer1 = nn.Linear(in_features=2, out_features=5)
        self.layer1 = nn.Linear(in_features=2, out_features=10) # increase units

        # in_features has to match with previous out_features
        # self.layer2 = nn.Linear(in_features=5, out_features=1)
        self.layer2 = nn.Linear(in_features=10, out_features=10) # increase units

        # more layers = better learning
        self.layer3 = nn.Linear(in_features=10, out_features=1)

        # non-linear activation function since problem deals with circles
        self.relu = nn.ReLU()

    def forward(self, x): # nn.Sequential does the same
        return self.layer3(self.relu(self.layer2(self.relu(self.layer1(x)))))
        # x -> layer1 -> relu -> layer2 -> relu -> layer 3
        # changes negatives of each layer to 0 and keeps positives as they are

# x contains coordinates while y contains 0s or 1s depending on if point is inside circle
X, y = make_circles(n_samples=1000, noise=0.03, random_state=42)
# 1000 points if paired together

# X = [[x, y],   <-- shape for one X sample is (2)
#         [x, y],
#             ...]

# y = [1/0, 1/0, 1/0, ...] <-- shape for one Y sample is 0

# polars dataframe formatting
circles = pol.DataFrame({"X": X[:, 0], "Y": X[:, 1], "Label": y})

# visualization
## plt.scatter(X[:, 0], X[:, 1], c=y, s=5, cmap=plt.cm.winter)
## plt.show()

# convert numpy to torch tensors
xTensor = torch.from_numpy(X).type(torch.float)
yTensor = torch.from_numpy(y).type(torch.float)

# split data for train and test
xTrain, xTest, yTrain, yTest = train_test_split(xTensor, yTensor, test_size=0.2, random_state=42)
# numy or torch.utils.data.random_split both work

# assign to device
xTrain, yTrain = xTrain.to(device), yTrain.to(device)
xTest, yTest = xTest.to(device), yTest.to(device)

model = circleModel().to(device)

''' or
model = nn.Sequential(
    nn.Linear(in_features=2, out_features=10),
    nn.ReLU(),
    nn.Linear(in_features=10, out_features=10),
    nn.ReLU(),
    nn.Linear(in_features=10, out_features=1)
).to(device)
''' # which does the same

## print(model) # check model info
## print(next(model.parameters()).device) # check device
## print(model.state_dict()) # size (10, 2) for layer1.weight, (10) for layer1.bias and so forth...(10, 10)...

def accuracy(yPreds, yTrue): # if needed
    correct = torch.eq(yTrue, yPreds).sum().item() # returns number of yTrue == yPreds
    return correct / len(yPreds)

# lossFx = nn.BECLoss() # need to go through sigmoid activation before BECLoss
# BCEWithLogits expects yLogits while BCE expects predProbs
lossFx = nn.BCEWithLogitsLoss() # sigmoid activation
optim = torch.optim.SGD(params=model.parameters(), lr=0.1)
# LEARNING RATE is really IMPORTANT!!!
# Also, Adam is probably better of a choice than SGD

# train loop
for trial in range(10000):
    model.train()
    trLogits = model(xTrain).squeeze()
    #  trPredProbs is torch.sigmoid(trLogits)
    trPredLabels = torch.round(torch.sigmoid(trLogits))
    trLoss = lossFx(trLogits, yTrain) # BCEWithLogits needs logits
    trAcc = accuracy(trPredLabels, yTrain)
    optim.zero_grad()
    trLoss.backward()
    optim.step()

    # test loop
    model.eval()
    with torch.inference_mode():
        teLogits = model(xTest).squeeze()
        tePredLabels = torch.round(torch.sigmoid(teLogits))
        teLoss = lossFx(teLogits, yTest) # same here
        teAcc = accuracy(tePredLabels, yTest)

    if trial % 100 == 0:
        print("Trial: {} | TrLoss: {:.3f} | TeLoss: {:.3f} | TrAcc: {:.3f} | TeACC: {:.3f}".format(trial, trLoss, teLoss, trAcc, teAcc))