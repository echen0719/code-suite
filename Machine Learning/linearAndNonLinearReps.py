import torch
import torch.nn as nn
import matplotlib.pyplot as plt

def relu(x):
  return torch.maximum(torch.tensor(0), x)

def sigmoid(x):
  return 1 / (1 + torch.exp(-x))

tensor = torch.arange(-10, 10, 1, dtype=torch.float32)
plt.plot(tensor)

plt.plot(torch.relu(tensor))
plt.plot(relu(tensor))

plt.plot(torch.sigmoid(tensor))
plt.plot(sigmoid(tensor))

plt.show()