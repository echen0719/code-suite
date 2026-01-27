# https://colab.research.google.com/drive/1x8F35cMxxHav8XGPPbKLJlWQg1qhEe33

import torch
from torch import nn
from torch.utils.data import DataLoader

import torchvision
from torchvision import datasets
from torchvision import transforms

# https://github.com/mert-kurttutan/torchview
from torchview import draw_graph
import graphviz
import matplotlib.pyplot as plt
import random

device = 'cuda' if torch.cuda.is_available() else 'cpu'
torch.manual_seed(42)
torch.cuda.manual_seed(42)

classMappings = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def dataVisualization(dataLoader):
    figure = plt.figure(figsize=(9, 9))
    images, labels = next(iter(trainDataLoader))

    for i in range(9): # I have a 7/10 understanding what is happening here
        index = random.randint(0, len(images) - 1)
        img = images[index].squeeze() # it is 1x28x28 dimension anyways
        label = labels[index].item()
        ax = figure.add_subplot(3, 3, i + 1)
        ax.imshow(img)
        ax.axis('off')
        ax.set_title(classMappings[label])
    plt.show()

class MLPModel(nn.Module):
    def __init__(self, out_features=10):
        super().__init__()
        self.linearStack = nn.Sequential(
            nn.Flatten(), # set starts as (1, 28, 28); needs to turn into (784)

            # applies linear transformation from size x1 -> x2
            nn.Linear(784, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(p=0.3), # to prevent overfitting

            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),

            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(p=0.3),

            nn.Linear(128, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),

            nn.Linear(64, out_features), # final size becames (10)
            nn.LogSoftmax(dim=1) # converts to probabilities
        )
    def forward(self, x):
        return self.linearStack(x)

def trainModel(numTrials, model, lossFx, optim, trainDataLoader):
    model.train()
    model.to(device)
    accuTrLoss, accuTrAcc = 0, 0
    losses, accuracies = [], []

    print('-- Training --')
    for trial in range(numTrials):
        for image, label in trainDataLoader:
            image, label = image.to(device), label.to(device)
            optim.zero_grad()
            output = model(image)

            # lossFx compares output with label; then loss is added up
            trLoss = lossFx(output, label)
            accuTrLoss += trLoss.item()

            # torch.max(output, 1) finds the highest probability value of output
            _, predicted = torch.max(output, 1)
            # checks if prediction and label match (index)
            accuTrAcc += (predicted == label).sum().item() # .sum() to add 0/1 for T/F

            trLoss.backward()
            optim.step() # changes optim values

        # trainDataLoader is 60,000/batch_size so .dataset gets the 60,000 instead
        accuTrLoss /= len(trainDataLoader.dataset) # accumulated average
        accuTrAcc /= len(trainDataLoader.dataset) # accumulated average

        print('Trial {}: TrLoss: {:3f} | TrAcc: {:3f}'.format(trial + 1, accuTrLoss, accuTrAcc))
        losses.append(accuTrLoss)
        accuracies.append(accuTrAcc)
    return losses, accuracies

def testModel(numTrials, model, lossFx, optim, testDataLoader):
    model.eval()
    model.to(device)
    accuTeLoss, accuTeAcc = 0, 0
    losses, accuracies = [], []

    with torch.no_grad():
        print('-- Testing --')
        for trial in range(numTrials):
            for image, label in testDataLoader:
                image, label = image.to(device), label.to(device)
                output = model(image)

                # lossFx compares output with label; then loss is added up
                teLoss = lossFx(output, label)
                accuTeLoss += teLoss.item()

                # torch.max(output, 1) finds the highest probability value of output
                _, predicted = torch.max(output, 1)
                # checks if prediction and label match (index)
                accuTeAcc += (predicted == label).sum().item() # .sum() to add 0/1 for T/F

            # trainDataLoader is 60,000/batch_size so .dataset gets the 60,000 instead
            accuTeLoss /= len(testDataLoader.dataset) # accumulated average
            accuTeAcc /= len(testDataLoader.dataset) # accumulated average

            print('Trial {}: TeLoss: {:3f} | TeAcc: {:3f}'.format(trial + 1, accuTeLoss, accuTeAcc))
            losses.append(accuTeLoss)
            accuracies.append(accuTeAcc)
        return losses, accuracies

def modelPredict(model, tensor): # takes in the model and a torch tensor
    plt.figure(figsize=(3, 3))
    plt.imshow(tensor.squeeze()) # convert [1, 28, 28] to [28, 28]
    plt.axis('off')
    plt.show()

    model.eval()
    model.to(device)
    output = model(tensor)

    with torch.no_grad():
        _, predicted = torch.max(output, 1)
        print("I predict: {}".format(classMappings[predicted]))

def visualizeResults(losses, accuracies, numTrials, title):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1) # creates a subplot with 1 row, 2 columns, at the left
    plt.plot(range(1, numTrials + 1), losses, label='{} Loss'.format(title))
    plt.xlabel('Trials')
    plt.ylabel('Loss')
    plt.legend()

    plt.subplot(1, 2, 2) # creates a subplot with 1 row, 2 columns, at the right
    plt.plot(range(1, numTrials + 1), accuracies, label='{} Accuracy'.format(title))
    plt.xlabel('Trials')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

def main(numTrials):
    trainData = datasets.FashionMNIST(root='data', train=True, download=True, transform=transforms.ToTensor())
    testData = datasets.FashionMNIST(root='data', train=False, download=True, transform=transforms.ToTensor())

    trainDataLoader = DataLoader(trainData, batch_size=64, shuffle=True)
    testDataLoader = DataLoader(testData, batch_size=64, shuffle=False)
    ## dataVisualization(trainDataLoader)

    model = MLPModel().to(device)
    modelGraph = draw_graph(model, input_size=(64, 784), expand_nested=True)
    # .render() from graphviz to export graph as png image
    ## modelGraph.visual_graph.render('model_design', format='png', cleanup=True)

    lossFx = nn.NLLLoss()
    optim = torch.optim.Adam(params=model.parameters(), lr=0.01)

    trLosses, trAccuracies = trainModel(numTrials, model, lossFx, optim, trainDataLoader)
    teLosses, teAccuracies = testModel(3, model, lossFx, optim, testDataLoader)

    ## visualizeResults(trLosses, trAccuracies, numTrials, 'Train')
    ## visualizeResults(teLosses, teAccuracies, 5, 'Test') # not really that useful to plot this

    images, _ = next(iter(trainDataLoader))
    randImg = images[random.randint(0, len(images) - 1)]
    modelPredict(model, randImg)

if __name__ == '__main__':
    main(32)

''' Results:
data/Model\\ Results/32-trial-loss⁄accuracy-FashionMNIST-MLP.png

-- Training --
Trial 1: TrLoss: 0.008731 | TrAcc: 0.800817
Trial 2: TrLoss: 0.006823 | TrAcc: 0.845330
Trial 3: TrLoss: 0.006173 | TrAcc: 0.859131
Trial 4: TrLoss: 0.005834 | TrAcc: 0.866498
Trial 5: TrLoss: 0.005540 | TrAcc: 0.871598
Trial 6: TrLoss: 0.005235 | TrAcc: 0.876948
Trial 7: TrLoss: 0.005102 | TrAcc: 0.880798
Trial 8: TrLoss: 0.004932 | TrAcc: 0.884715
Trial 9: TrLoss: 0.004681 | TrAcc: 0.889481
Trial 10: TrLoss: 0.004579 | TrAcc: 0.893031
Trial 11: TrLoss: 0.004417 | TrAcc: 0.896615
Trial 12: TrLoss: 0.004289 | TrAcc: 0.899348
Trial 13: TrLoss: 0.004183 | TrAcc: 0.901565
Trial 14: TrLoss: 0.004087 | TrAcc: 0.903782
Trial 15: TrLoss: 0.003998 | TrAcc: 0.906065
Trial 16: TrLoss: 0.003875 | TrAcc: 0.908515
Trial 17: TrLoss: 0.003764 | TrAcc: 0.912548
Trial 18: TrLoss: 0.003672 | TrAcc: 0.914332
Trial 19: TrLoss: 0.003590 | TrAcc: 0.914649
Trial 20: TrLoss: 0.003518 | TrAcc: 0.916532
Trial 21: TrLoss: 0.003402 | TrAcc: 0.918582
Trial 22: TrLoss: 0.003383 | TrAcc: 0.919565
Trial 23: TrLoss: 0.003270 | TrAcc: 0.922382
Trial 24: TrLoss: 0.003271 | TrAcc: 0.922315
Trial 25: TrLoss: 0.003177 | TrAcc: 0.924749
Trial 26: TrLoss: 0.003097 | TrAcc: 0.927132
Trial 27: TrLoss: 0.003046 | TrAcc: 0.927732
Trial 28: TrLoss: 0.003004 | TrAcc: 0.929149
Trial 29: TrLoss: 0.002942 | TrAcc: 0.929565
Trial 30: TrLoss: 0.002907 | TrAcc: 0.930015
Trial 31: TrLoss: 0.002839 | TrAcc: 0.933382
Trial 32: TrLoss: 0.002758 | TrAcc: 0.934849
-- Testing --
Trial 1: TeLoss: 0.004855 | TeAcc: 0.902100
Trial 2: TeLoss: 0.004855 | TeAcc: 0.902190
Trial 3: TeLoss: 0.004855 | TeAcc: 0.902190
'''