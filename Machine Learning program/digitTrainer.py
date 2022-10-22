import keras
import numpy
import tensorflow as tf
import time
import pygame


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test,y_test) = mnist.load_data()
print(repr(x_train.shape))
print(repr(y_train.shape))
print(repr(x_test.shape))
print(repr(y_test.shape))
inputx = input("Continue?(Y/N):")
if inputx != "Y":
    quit()



model = keras.models.load_model("digit2")
# model = tf.keras.models.Sequential([
#   tf.keras.layers.Flatten(input_shape=(28, 28)),
#   tf.keras.layers.Dense(256, activation='relu'),
#   tf.keras.layers.Dense(256, activation='relu'),
#     tf.keras.layers.Dense(256, activation='relu'),
#     tf.keras.layers.Dense(256, activation='relu'),
#      tf.keras.layers.Dense(256, activation='relu'),
#     tf.keras.layers.Dense(256, activation='relu'),
#     tf.keras.layers.Dense(256, activation='relu'),
#     tf.keras.layers.Dense(2016, activation='relu'),
#   tf.keras.layers.Dense(256)
# ])
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
predictions = model(x_train[:1]).numpy()
tf.nn.softmax(predictions).numpy()
loss_fn(y_train[:1], predictions).numpy()
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_test, y_test, epochs=25)
model.fit(x_train, y_train, epochs=25)
print(model.evaluate(x_train,  y_train, verbose=1))
print(model.evaluate(x_test,  y_test, verbose=1))
model.save('digit2')


