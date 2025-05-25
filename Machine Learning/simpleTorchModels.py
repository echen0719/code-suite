# check this out: https://www.learnpytorch.io/01_pytorch_workflow/

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# class to calculate y = mx + b
class LinearRegModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1, dtype=torch.float32))
        self.bias = nn.Parameter(torch.randn(1, dtype=torch.float32))

    def forward(self, x):
        return self.weights * x + self.bias

''' Honestly, this would have worked
def forward(x):
    weights = nn.Parameter(torch.randn(1, dtype=torch.float32, requires_grad=True))
    bias = nn.Parameter(torch.randn(1, dtype=torch.float32, requires_grad=True))
    return weights * x + bias
'''

# matplotlib plotter, nothing special
def trainAndTestPlotter(xTrain, yTrain, trainLabel, xTest, yTest, testLabel):
    plt.scatter(xTrain, yTrain, label=trainLabel)
    plt.scatter(xTest, yTest, label=testLabel)
    plt.legend(); plt.show()

def linearReg(m=0.75, b=0.25, start=0, end=1, step=0.05):
    # forms an (x, y) table
    x = torch.arange(start, end + step, step)
    y = m * x + b

    # 80% data used for training, 20% for testing
    split = int(0.8 * len(x))
    xTrain, yTrain = x[:split], y[:split] # 80%
    xTest, yTest = x[split:], y[split:] # 20%

    # trainAndTestPlotter(xTrain, yTrain, "Train", xTest, yTest, "Test")

    torch.manual_seed(42)
    model1 = LinearRegModel()
    with torch.inference_mode():
        yPreds = model1(xTest)

    trainAndTestPlotter(xTrain, yTrain, "Train", xTest, yPreds, "Test")

linearReg()