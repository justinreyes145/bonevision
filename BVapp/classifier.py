import tensorflow as tf
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

def thread_load_frac_model(model, weights_path):
    st = time.time()
    model.load_weights(weights_path)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    print(f'Time elapsed = {time.time() - st} sec (' + weights_path + ")")
    return model

def thread_load_bone_model(model):
    st = time.time()
    model.load_weights('models/bone_weights.keras')
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    print(f'Time elapsed = {time.time() - st} sec (Bone Model)')
    return model

# Load all model architectures
global bone_model = load_bone_model()
global elbow_model = load_frac_model()
global finger_model = load_frac_model()
global forearm_model = load_frac_model()
global hand_model = load_frac_model()
global humerus_model = load_frac_model()
global shoulder_model = load_frac_model()
global wrist_model = load_frac_model()

t0 = threading.Thread(target=thread_load_bone_model, args=(bone_model,))
t0.start()
t1 = threading.Thread(target=thread_load_frac_model, args=(wrist_model, 'models/wrist_86.65_weights.keras'))
t1.start()
t2 = threading.Thread(target=thread_load_frac_model, args=(humerus_model, 'models/humerus_88.89_weights.keras'))
t2.start()
t3 = threading.Thread(target=thread_load_frac_model, args=(forearm_model, 'models/forearm_80.07_weights.keras'))
t3.start()
t4 = threading.Thread(target=thread_load_frac_model, args=(hand_model, 'models/hand_79.96_weights.keras'))
t4.start()
t5 = threading.Thread(target=thread_load_frac_model, args=(elbow_model, 'models/elbow_86.67_weights.keras'))
t5.start()
t6 = threading.Thread(target=thread_load_frac_model, args=(shoulder_model, 'models/shoulder_81.53_weights.keras'))
t6.start()
t7 = threading.Thread(target=thread_load_frac_model, args=(finger_model, 'models/finger_80.04_weights.keras'))
t7.start()

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

def predict(model, image_path):
    # model not loaded
    if model == None:
        return None
        
    # weights not loaded
    if not model.weights:
        return None
    image = load_image(image_path, 512)
    return model.predict(image)

def predict_bone(image_path):
    # model not loaded
    if bone_model == None:
        return None
        
    # weights not loaded
    if not bone_model.weights:
        return None
    image = load_image(image_path, 224)
    return bone_model.predict(image)

def predict_image():
    image_path = ('temp')
    image = load_image(image_path, 224)
    bone_type = np.array(predict(bone_model, image_path))
    max_index = np.argmax(bone_type[0])
    print(bone_type)
    print(max_index)
    fracture_prediction = None

    match max_index:
        case 0:
            fracture_prediction = 1 - predict(elbow_model, image_path)
        case 1:
            fracture_prediction = 1 - predict(finger_model, image_path)
        case 2:
            fracture_prediction = 1 - predict(forearm_model, image_path)
        case 3:
            fracture_prediction = 1 - predict(hand_model, image_path)
        case 4:
            fracture_prediction = 1 - predict(humerus_model, image_path)
        case 5:
            fracture_prediction = 1 - predict(shoulder_model, image_path)
        case 6:
            fracture_prediction = 1 - predict(wrist_model, image_path)
        case 7:
            return None

    result = f'{fracture_prediction[0] * 100}% chance of {bone_labels[max_index]} fracture'
    print(result)
