import torch
from tqdm import tqdm
import numpy as np

def accuracy(yPreds, yTrue):
    correct = torch.eq(yTrue, yPreds).sum().item()
    return correct / len(yPreds)

def trainStep(model, dataLoader, lossFx, optim, accuracy, device, scheduler=None, useTQDM=False):
    if useTQDM: dataLoader = tqdm(dataLoader, desc="Training")
    accuLoss, accuAcc = 0, 0
    model.to(device); model.train()
    for batch, (image, label) in enumerate(dataLoader):
        image, label = image.to(device), label.to(device)
        logits = model(image)
        loss = lossFx(logits, label)
        accuLoss += loss
        accuAcc += accuracy(logits.argmax(dim=1), label)
        optim.zero_grad()
        loss.backward()
        optim.step()
        if scheduler:
            scheduler.step()
    accuLoss /= len(dataLoader)
    accuAcc /= len(dataLoader)
    print("TrLoss: {:3f} | TrAcc: {:3f} | ".format(accuLoss, accuAcc), end='')

def testStep(model, dataLoader, lossFx, optim, accuracy, device, useTQDM=False):
    if useTQDM: dataLoader = tqdm(dataLoader, desc="Testing")
    accuLoss, accuAcc = 0, 0
    model.to(device); model.eval()
    with torch.inference_mode():
        for batch, (image, label) in enumerate(dataLoader):
            image, label = image.to(device), label.to(device)
            logits = model(image)
            accuLoss += lossFx(logits, label)
            accuAcc += accuracy(logits.argmax(dim=1), label)
        accuLoss /= len(dataLoader)
        accuAcc /= len(dataLoader)
        print("TeLoss: {:3f} | TeAcc: {:3f}".format(accuLoss, accuAcc))

def decodeSegmap(image, classCount):
    # all of these colors represent a different class
    labelColors = np.array([
        (0, 0, 0), (128, 0, 0), (0, 128, 0), # black, maroon, dark green
        (128, 128, 0), (0, 0, 128),  (128, 0, 128), # dark yellow, dark blue, dark magenta
        (0, 128, 128), (128, 128, 128), (64, 0, 0), # dark teal, gray, brown
        (192, 0, 0), (64, 128, 0), (192, 128, 0), # dark red, lighter green, orange
        (64, 0, 128), (192, 0, 128), (64, 128, 128), # purple, dark pink, lighter teal
        (192, 128, 128), (0, 64, 0), (128, 64, 0), # pink, really dark green, lighter brown
        (0, 192, 0), (128, 192, 0), (0, 64, 128), # real green, green-yellow, lighter blue
    ])

    r = np.zeros_like(image).astype(np.uint8)
    g = np.zeros_like(image).astype(np.uint8)
    b = np.zeros_like(image).astype(np.uint8)

    for i in range(0, classCount):
        idx = image == i # where the image has a class at i
        r[idx] = labelColors[i, 0]
        g[idx] = labelColors[i, 1]
        b[idx] = labelColors[i, 2]

    rgb = np.stack([r, g, b], axis=2) # idk what this is
    return rgb