import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print('Tensorflow version:',tf.__version__)
import numpy as np
import pandas as pd
import cv2

def prepare():
    img_array = cv2.imread("face.jpg")
    new_array = cv2.resize(img_array, (64, 64))
    return new_array.reshape(-1, 64, 64, 1)
    
model = tf.keras.models.load_model("emotion_model.hdf5")
prediction = model.predict(prepare())
print(prediction)