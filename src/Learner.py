import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

from SampleDataGenerator import SampleDataGenerator

print(dir(SampleDataGenerator))

SAMPLE_SIZE = 100_000
SAMPLES = []
SAMPLE_LABELS = []

for sample in SampleDataGenerator.generateSamples(SAMPLE_SIZE):
    SAMPLES.append(sample[0])
    SAMPLE_LABELS.append(sample[1])

SAMPLES = np.array(SAMPLES)
SAMPLE_LABELS = np.array(SAMPLE_LABELS)

print(SAMPLES)

model = keras.Sequential([
    keras.layers.Dense(4, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(5, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(SAMPLES, SAMPLE_LABELS, epochs=5)

model.save_weights("./weights")

# model.load_weights("./weights")

test_samples = []
test_labels = []

for sample in SampleDataGenerator.generateSamples(500):
    test_samples.append(sample[0])
    test_labels.append(sample[1])

test_samples = np.array(test_samples)
test_labels = np.array(test_labels)

test_loss, test_acc = model.evaluate(test_samples, test_labels)
print('Test accuracy:', test_acc)

print(test_samples[10], end=" ")
print(test_labels[10])
print(test_samples.shape)

to_predict = np.array([test_samples[10]])
print(to_predict.shape)

print(model.predict(to_predict) * 10)


plt.imshow(np.array([test_samples[10][0:2] * 255, test_samples[10][2:] * 255]), cmap="gray")
plt.show()

