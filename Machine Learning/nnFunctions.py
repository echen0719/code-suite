import torch

def accuracy(yPreds, yTrue):
    correct = torch.eq(yTrue, yPreds).sum().item()
    return correct / len(yPreds)

def trainStep(model, dataLoader, lossFx, optim, accuracy, device, scheduler=None):
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

def testStep(model, dataLoader, lossFx, optim, accuracy, device):
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
