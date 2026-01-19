import torch
from torchvision import transforms
from PIL import Image
# from *modelClass* import *model*

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
## model = CNNModel(3, 10, hidden_units=10).to(device) # change per file
## classMappings = # change per file

def prepareImage(imagePath):
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor()
    ])

    image = Image.open(imagePath).convert('RGB')
    tensor = transform(image).unsqueeze(0).to(device)
    # dimension of batch size needs to exist

    return tensor

def visualizeImage(tensor):
    plt.imshow(tensor[0].permute(1, 2, 0).cpu())
    plt.axis('off')
    plt.show()

def modelEvaluate(model, topK):
    model.eval()
    model.to(device)

    with torch.no_grad():
        output = model(tensor) # [1, output] format
        probs = nn.functional.softmax(output, dim=1).squeeze()

        indicies = torch.argsort(probs, descending=True)
        # indicies output ex.: tensor([6, 3, 7, 5, 4, 9, 2, 0, 1, 8])

        for i in range(topK):
          index = indicies[i].item() # gets mapping and probs for indicies[i -> topK]
          print('{}: {:5f}'.format(classMappings[index], probs[index].item()))

model.load_state_dict(torch.load(input('What is the model path? ')))
tensor = prepareImage(input('What is the image path? '))

visualizeImage(tensor)
modelEvaluate(model)