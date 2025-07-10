# image_preprocessing.py

from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
import numpy as np
import os
from config import IMAGE_DIR

def extract_features():
    model = VGG16()
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    
    features = {}
    for img_name in os.listdir(IMAGE_DIR):
        filename = os.path.join(IMAGE_DIR, img_name)
        image = load_img(filename, target_size=(224, 224))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = preprocess_input(image)
        feature = model.predict(image, verbose=0)
        features[img_name] = feature
    return features
