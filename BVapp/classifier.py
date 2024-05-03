import os

import tensorflow as tf
from PySide6.QtWidgets import QMessageBox
from keras_preprocessing.image import ImageDataGenerator
from tensorflow import keras
import numpy as np
import time
from skimage import transform
from skimage.io import imread

import threading

def load_frac_model():
    with open('models/model.json', 'r') as model_data:
        loaded_model_json = model_data.read()
        return keras.models.model_from_json(loaded_model_json)


def load_bone_model():
    with open('models/bone_model.json', 'r') as model_data:
        loaded_model_json = model_data.read()
        return keras.models.model_from_json(loaded_model_json)

def thread_load_all_models():
    st = time.time()
    bone_model = load_bone_model()
    bone_model.load_weights('models/bone_weights.keras')
    bone_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    elbow_model = load_frac_model()
    elbow = True
    print(f'Time elapsed = {time.time() - st} sec (Elbow)')

    finger_model = keras.models.load_model('models/dense169_finger_70_07_acc.keras', compile=False)
    finger = True

    forearm_model = keras.models.load_model('models/dense169_forearm_75_75_acc.keras', compile=False)
    forearm = True

    hand_model = load_frac_model()
    hand = True

    humerus_model = load_frac_model()
    humerus = True

    shoulder_model = keras.models.load_model('models/dense169_shoulder_70_69_acc.keras', compile=False)
    shoulder = True

    wrist_model = keras.models.load_model('models/dense169_wrist_75_42_acc.keras', compile=False)
    wrist = True

    print(f'Time elapsed = {time.time() - st} sec (Bone)')
    st = time.time()
    

# Load all model architectures
bone_model = None
elbow_model = None
finger_model = None
forearm_model = None
hand_model = None
humerus_model = None
shoulder_model = None
wrist_model = None
model_loading_thread = threading.Thread(target=thread_load_all_models)
model_loading_thread.start()

bone_labels = ['ELBOW', 'FINGER', 'FOREARM', 'HAND', 'HUMERUS', 'SHOULDER', 'WRIST']

def load_image(image_path, size):
    data_generator = ImageDataGenerator(
        rescale=1./255
    )

    test_data_generator = data_generator.flow_from_directory(
        image_path,
        target_size=(size, size),
        batch_size=1,
        class_mode='binary'
    )
    img, lbl = next(test_data_generator)

    return img


def predict_elbow(image_path):
    global elbow
    if elbow:
        # Wait for model load
        while elbow_model == None:
            continue
        st = time.time()
        elbow_model.load_weights('models/elbow_86.67_weights.keras')
        elbow_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (Elbow)')
        elbow = False
    image = load_image(image_path, 512)
    return elbow_model.predict(image)


def predict_finger(image_path):
    global finger
    if finger:
        # Wait for model load
        while finger_model == None:
            continue
        st = time.time()
        finger_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (Finger)')
        finger = False
    image = load_image(image_path, 224)
    return finger_model.predict(image)


def predict_forearm(image_path):

    global forearm
    if forearm:
        # Wait for model load
        while forearm_model == None:
            continue
        st = time.time()
        forearm_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (Forearm)')
        forearm = False
    image = load_image(image_path, 224)
    return forearm_model.predict(image)


def predict_hand(image_path):
    global hand
    if hand:
        # Wait for model load
        while hand_model == None:
            continue
        st = time.time()
        hand_model.load_weights('models/hand_79.96_weights.keras')
        hand_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (Hand)')
        hand = False
    image = load_image(image_path, 512)
    return hand_model.predict(image)


def predict_humerus(image_path):
    global humerus
    if humerus:
        # Wait for model load
        while humerus_model == None:
            continue
        st = time.time()
        humerus_model.load_weights('models/humerus_88.89_weights.keras')
        humerus_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (Humerus)')
        humerus = False
    image = load_image(image_path, 512)
    return humerus_model.predict(image)


def predict_shoulder(image_path):
    global shoulder
    if shoulder:
        # Wait for model load
        while shoulder_model == None:
            continue
        st = time.time()
        shoulder_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (Shoulder)')
        shoulder = False
    image = load_image(image_path, 224)
    return shoulder_model.predict(image)


def predict_wrist(image_path):
    global wrist
    if wrist:
        # Wait for model load
        while wrist_model == None:
            continue
        st = time.time()
        wrist_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (Wrist)')
        wrist = False
    image = load_image(image_path, 224)
    return wrist_model.predict(image)


def predict_bone(image_path):
    image = load_image(image_path, 224)
    return bone_model.predict(image)

def predict_image():
    if not os.path.exists('temp'):  # Check if image exists
        QMessageBox.warning(None, "Warning", "No image uploaded!", QMessageBox.Ok)
        return

    image_path = 'temp'
    bone_type = np.array(predict_bone(image_path))
    max_index = np.argmax(bone_type[0])
    print(bone_type)
    print(max_index)
    fracture_prediction = None

    match max_index:
        case 0:
            fracture_prediction = 1 - predict_elbow(image_path)
        case 1:
            fracture_prediction = 1 - predict_finger(image_path)
        case 2:
            fracture_prediction = 1 - predict_forearm(image_path)
        case 3:
            fracture_prediction = 1 - predict_hand(image_path)
        case 4:
            fracture_prediction = 1 - predict_humerus(image_path)
        case 5:
            fracture_prediction = 1 - predict_shoulder(image_path)
        case 6:
            fracture_prediction = 1 - predict_wrist(image_path)
        case 7:
            return None

    result = f'{fracture_prediction[0] * 100}% chance of {bone_labels[max_index]} fracture'
    print(result)
    QMessageBox.information(None, "Fracture Prediction", result, QMessageBox.Ok)

