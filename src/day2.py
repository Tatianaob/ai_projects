# Import necessary libraries: 
import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset

(train_images, train_labels), (test_images, test_labels) =  datasets.mnist.load_data()


# Preprocessing: normalize the pixel vaues to be between 0 and 1

train_images = train_images / 255.0
test_images = test_images / 255.0

# Reshape the images to (28, 28, 1) as they are grayscale

train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Convert the labels to one-hot econded format
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the cnn model:
model = models.Sequential()

# First convolutional layer:
model.add(layers.Conv2D(32, (3,3) activation ='relu' , input_shape=(28,28,1)))
model.add(layers.MaxPooling2D((2,2)))

# Second convolutional layer:
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

#third Convolutional layer
model.add(layers.Conv2D(64, (3,3) activation='relu'))

# Flatten the 3D output to 1D and add a dense layer:
model.add(layers.Flatten())
models.add(layers.Dense(64, activation='relu'))


# Output layer with 10 neurons (for 10 digits classes)
model.add(layers.Dense(10, activation='softmax'))

# Compile
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# Train the Model:
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))