# check this out: https://www.learnpytorch.io/01_pytorch_workflow/

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

torch.manual_seed(42)

def plot(trData, trLabels, teData, teLabels, predLabels=None):
    # train data
    plt.scatter(trData, trLabels, c='r', label='Train')
    # test data
    plt.scatter(teData, teLabels, c='b', label='Test')

    # Y predictions from xTest
    if predLabels is not None:
        plt.scatter(teData, predLabels, c='g', label='Predictions')

    plt.legend()
    plt.show()

'''
starts with random weights and biases looks at training
data and adjust these values to be closer to wanted data
with gradient descent and/or backpropagation
'''

# standard model setup
class linRegModel(nn.Module):
    def __init__(self):
        super().__init__()
        # require_grad=true (grad meaning gradients)
        self.weight = nn.Parameter(torch.randn(1, dtype=torch.float))
        self.bias = nn.Parameter(torch.randn(1, dtype=torch.float))
        ## self.linear = nn.Linear(1, 1) # <-- same

    # forward overwritten, x is input tensor
    def forward(self, x):
        return self.weight * x + self.bias # actual linear reg
        ## return self.linear(x) # also linear reg

# y = mx + b
weight = 0.7 # m
bias = 0.3 # b

# 0 <= x <= 1
xTensor = torch.arange(0, 1, 0.02).unsqueeze(dim=1)
y = weight * xTensor + bias

# split into train and test sets
split = int(0.7 * len(xTensor))
xTrain, yTrain = xTensor[:split], y[:split]
xTest, yTest = xTensor[split:], y[split:]

model = linRegModel()
## print(model.state_dict()) # original

# inference mode turns off gradient
# with torch.inference_mode(): # .no_grad() also works
    # yPreds = model(xTest)

# plot(xTrain, yTrain, xTest, yTest, predLabels=yPreds)

# https://docs.pytorch.org/docs/stable/nn.html#loss-functions
# loss functions - functions to determine inaccuracy
lossFx = nn.L1Loss()

# https://docs.pytorch.org/docs/stable/optim.html#algorithms
# optimizer - functions to shift weights and biases
optim = torch.optim.SGD(params=model.parameters(), lr=0.01)
# learning rate is the increment parameters change

# training loop
for trial in range(100):
    # gradients have to be enabled for backpropagation to work
    model.train() # all parameters requiring gradients will
    trPreds = model(xTrain) # forward pass
    trLoss = lossFx(trPreds, yTrain) # loss calculation
    optim.zero_grad() # set back to zero after each loop
    trLoss.backward() # backpropagation
    optim.step() # increments the optimizer

    # testing loop
    model.eval() # put model.eval() inside if validating after each trial
    with torch.inference_mode():
        tePred = model(xTest) # forward
        teLoss = lossFx(tePred, yTest) # find loss

    if trial % 10 == 0:
        print("Trial: {} | Training Loss: {} | Test loss: {}".format(trial, loss, teLoss))

with torch.inference_mode(): # or else model(xTest) doesn't work'
    plot(xTrain, yTrain, xTest, yTest, predLabels=model(xTest))
    # much better results than before

# save the model
torch.save(obj=model.state_dict(), f='models/simple-linear-reg.pth')

# load the model; must call class
newModel = linRegModel()
newModel.load_state_dict(torch.load(f='models/simple-linear-reg.pth'))