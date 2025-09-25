# This script builds, trains, and evaluates a Convolutional Neural Network (CNN)
#  on the MNIST dataset (handwritten digit images 0–9).

# It goes through the whole ML pipeline: data loading → preprocessing → model building → 
# training → evaluation → prediction → visualization.



# Import necessary libraries: 
import numpy as np #math and array operations
import tensorflow as tf    # deep learning
from keras import datasets, layers, models
from keras.utils import to_categorical
import matplotlib.pyplot as plt     #for plotting images and results

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Preprocessing: normalize the pixel values to be between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# Reshape the images to (28, 28, 1) as they are grayscale
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Convert the labels to one-hot encoded format
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the CNN model
model = models.Sequential()

# First convolutional layer
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)))
model.add(layers.MaxPooling2D((2,2)))

# Second convolutional layer
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

# Third convolutional layer
model.add(layers.Conv2D(64, (3,3), activation='relu'))

# Flatten the 3D output to 1D and add a dense layer
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

# Output layer with 10 neurons (for 10 digit classes)
model.add(layers.Dense(10, activation='softmax'))

# Compile
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the Model
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc * 100:.2f}%")

# Make predictions on test images
predictions = model.predict(test_images)
print(f"Prediction for first test image: {np.argmax(predictions[2])}")

# Plot the first test image with predicted label
plt.imshow(test_images[2].reshape(28,28), cmap='gray')
plt.title(f"Predicted label: {predictions[2].argmax()}")
plt.show()
