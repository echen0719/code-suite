# https://colab.research.google.com/drive/1TgyKAEn43Ejt2AY4-rreBn4iU3lZG_Uq
from nnFunctions import *

import torch

import torchvision
from torchvision import transforms
from torchvision.models import segmentation

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def plotRGB(rgb):
    plt.imshow(rgb)
    plt.axis('off')
    plt.show()

def main(imagePath):
    model = segmentation.deeplabv3_resnet101(weights='COCO_WITH_VOC_LABELS_V1').eval()
    image = Image.open(imagePath) # currently in the shape (C, H, W)

    transform = transforms.Compose([
            transforms.Resize(256), # resizes to 256x256
            transforms.ToTensor(),
            transforms.Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225]) # imageNet normalization values
    ])

    tensor = transform(image).unsqueeze(0).to(device) # currently in the shape (1, 3, 224, 224)
    output = model(tensor)['out']
    ## print(output.shape) # currently in the shape (1, 21, 224, 224)

    # copies an argmax tensor of (21, 224, 224) to cpu in an numpy array
    output = torch.argmax(output.squeeze(), dim=0).detach().cpu().numpy()
    ## print(np.unique(output)) # there are 15 unique classes in the image

    plotRGB(decodeSegmap(output, 21))

if __name__ == '__main__':
    main('data/boiidkifoundthisonline.jpg')
    main('data/lookatthisunicorn.jpeg')
    main('data/amaybehappyfamily.jpeg')