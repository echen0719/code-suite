import torch
import torch.nn as nn
import numpy as np
import polars as pol # faster than pandas
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

device = "cuda" if torch.cuda.is_available() else "cpu"
torch.manual_seed(42)

class circleModel(nn.Module):
    def __init__(self):
        super().__init__()
        # xTrain size is (800, 2)
        # yTrain size is (800)
        self.layer1 = nn.Linear(in_features=2, out_features=5)
        # in_features has to match with previous out_features
        self.layer2 = nn.Linear(in_features=5, out_features=1)

    def forward(self, x):
        return self.layer2(self.layer1(x)) # nn.Sequential does the same
        # x -> layer1 -> layer2

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
## plt.scatter(X[:, 0], X[:, 1], c=y, s=5, cmap=plt.cm.RdYlBu)
## plt.show()

# convert numpy to torch tensors
xTensor = torch.from_numpy(X).type(torch.float32)
yTensor = torch.from_numpy(y).type(torch.float32)

# split data for train and test
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=42)

model = circleModel().to(device) # or
model = nn.Sequential(
    nn.Linear(in_features=2, out_features=5),
    nn.Linear(in_features=5, out_features=1)
).to(device)

## print(next(model.parameters()).device) # check device
## print(model.state_dict()) # yeilds size (5, 2) for 0.weight and (5) for 0.bias

# lossFx = nn.BECLoss() # need to go through sigmoid activation before BECLoss
lossFx = nn.BECWithLogitsLoss() # sigmoid activation
optim = torch.optim.SGD(params=model.parameters(), lr=0.01)