# guide: https://keras.io/examples/vision/image_classification_from_scratch/
# and https://www.learnpytorch.io/03_pytorch_computer_vision/
# and https://keras.io/examples/vision/mnist_convnet/

import random
import numpy as np
import keras
from keras import layers
import tensorflow
from tensorflow.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt

# Model / data parameters
itemMap = ['T-Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Boot']
num_classes = 10
input_shape = (28, 28, 1)

def showExamplars(amount, images, labels):
  plt.figure(figsize=(10, 10))
  for i in range(amount):
    plt.subplot(4, int((amount + 3)/4), i + 1) # displays 4 rows of images with overflow
    randInt = random.randint(0, len(images) - 1)
    plt.imshow(images[randInt])
    plt.title(itemMap[int(labels[randInt])])
    plt.axis('off')

(xTrain, yTrain), (xTest, yTest) = fashion_mnist.load_data()

# showExamplars(21, xTrain, yTrain)

xTrain = np.expand_dims(xTrain, -1)
yTrain = keras.utils.to_categorical(yTrain, num_classes)
xTest = np.expand_dims(xTest, -1)
yTest = keras.utils.to_categorical(yTest, num_classes)

print(xTrain.shape)
print(yTrain.shape)
print(xTest.shape)
print(yTest.shape)

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(xTrain, yTrain, batch_size=128, epochs=15)
