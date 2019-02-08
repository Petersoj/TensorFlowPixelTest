import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

from SampleDataGenerator import SampleDataGenerator

print(dir(SampleDataGenerator))

SAMPLE_SIZE = 50000
SAMPLES = []
SAMPLE_LABELS = []

for sample in SampleDataGenerator.generateSamples(SAMPLE_SIZE):
    SAMPLES.append(sample[0])
    SAMPLE_LABELS.append(sample[1])

SAMPLES = np.array(SAMPLES)
SAMPLE_LABELS = np.array(SAMPLE_LABELS)

print(SAMPLES)

model = keras.Sequential([
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(SAMPLES, SAMPLE_LABELS, epochs=5)

test_samples = []
test_labels = []
for sample in SampleDataGenerator.generateSamples(5000):
    test_samples.append(sample[0])
    test_labels.append(sample[1])

test_samples = np.array(test_samples)
test_labels = np.array(test_labels)

test_loss, test_acc = model.evaluate(test_samples, test_labels)
print('Test accuracy:', test_acc)