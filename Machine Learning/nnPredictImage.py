import torch
from torchvision import transforms
from PIL import Image
# from *modelClass* import *model*

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
## model = CNNModel(3, 10, hidden_units=10).to(device) # change per file

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

def modelEvaluate(model):
    model.eval()
    model.to(device)
    output = model(tensor)

    with torch.no_grad():
        _, predicted = torch.max(output, 1)
        print('I predict: {}'.format(classMappings[predicted]))

model.load_state_dict(torch.load(input('What is the model path? ')))
tensor = prepareImage(input('What is the image path? '))

visualizeImage(tensor)
modelEvaluate(model)