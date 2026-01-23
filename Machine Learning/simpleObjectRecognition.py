# https://colab.research.google.com/drive/12TtWMvdoOgK9nGqMejGAIgmu-HtSyglC
# Objection recognition is just CNN but using regions to assign classes

import torch

import torchvision
from torchvision import transforms
from torchvision.models import detection

import requests
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
categoryNames = [
        '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A',
        'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe',
        'N/A', 'backpack', 'umbrella', 'N/A', 'N/A', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite',
        'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
        'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant',
        'bed', 'N/A', 'dining table', 'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
    ] # 91 categories which a bunch of them being 'N/A' for some reason
colors = np.random.uniform(0, 255, size=(91, 3)) # 91 random colors for each class

def requestImages():
    urls = ['https://learnopencv.com/wp-content/uploads/2022/10/people.jpg', 'https://learnopencv.com/wp-content/uploads/2022/10/traffic_scene.jpg', 'https://learnopencv.com/wp-content/uploads/2022/10/night-time.jpg', 'https://learnopencv.com/wp-content/uploads/2022/10/crowd.jpg']
    fileNames = ['people', 'traffic_scene', 'night-time', 'crowd']

    for i in range(len(urls)):
        request = requests.get(urls[i])

        if request.status_code == 200:
            with open('data/{}'.format(fileNames[i]), 'wb') as file:
                file.write(request.content)
                print('Got {}'.format(fileNames[i]))
        else:
            print('Check it out yourself')

def modelPredict(predictions):
    # three things: the area, the label, and the confidence
    boxes = predictions['boxes'].detach().cpu().numpy()
    labels = predictions['labels'].detach().cpu().numpy()
    scores = predictions['scores'].detach().cpu().numpy()
    validIndices = scores > 0.5 # filter so only confident ones are kept

    predictionBoxes = []
    predictionClasses = []

    # basically for each, it gets the top left corner and bottom right corner to draw a rectangle
    for box in boxes[validIndices]:
        topLeft = (int(box[0]), int(box[1]))
        bottomRight = (int(box[2]), int(box[3]))
        predictionBoxes.append((topLeft, bottomRight))

    # this just gets the predicted class name so it can be used later on
    for label in labels[validIndices]:
        predictionClasses.append(categoryNames[label])

    return predictionBoxes, predictionClasses

def viewCVImage(imagePath, boxes, labels):
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # so i think openCV uses BGR instead, huh

    # it just works so I copied -- it determine the thickness for rectangle borders and the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    rectThickness = max(round(sum(image.shape) / 2 * 0.003), 2)
    textThickness = max(rectThickness - 1, 1)

    for i in range(len(boxes)):
        # boxes format is boxes = [ ( (), () ) , ( (), () ) , ( (), () ), ...]
        topLeft, bottomRight = boxes[i]
        color = colors[categoryNames.index(labels[i])]

        cv2.rectangle(image, topLeft, bottomRight, color=color, thickness=rectThickness) # makes a box around object

        # this calculates the width and height of the generated text
        (textWidth, textHeight), _ = cv2.getTextSize(labels[i], 0, fontScale=rectThickness/3, thickness=textThickness) # don't need baseline
        xOrigin, yOrigin = topLeft[0], topLeft[1]

        # background moves up by textHeight and a padding of 6 pixels
        # background is padded on the right by 6 pixels and the bottom by 4
        cv2.rectangle(image, (xOrigin, yOrigin - textHeight - 6), (xOrigin + textWidth + 6, yOrigin + 4), color=color, thickness=-1)
        cv2.putText(image, labels[i], (xOrigin + 3, yOrigin - 3), font, fontScale=rectThickness/3, color=(255, 255, 255), thickness=textThickness)

    plt.figure(figsize=(10, 6))
    plt.imshow(image)
    plt.show()

def main(imagePath):
    weights = detection.FasterRCNN_ResNet50_FPN_Weights.DEFAULT
    model = detection.fasterrcnn_resnet50_fpn(weights=weights).eval()
    ## print(weights.meta['categories']) # gets the names of trained classes

    image = Image.open(imagePath)
    transform = transforms.Compose([transforms.ToTensor()])
    tensor = transform(image)

    boxes, labels = modelPredict(model([tensor])[0])
    viewCVImage(imagePath, boxes, labels)

if __name__ == '__main__':
    requestImages()
    main('data/people')
    main('data/traffic_scene')
    main('data/night-time')
    main('data/crowd')