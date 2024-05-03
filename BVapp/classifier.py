import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
from tensorflow import keras
import numpy as np
import time
from skimage import transform
from skimage.io import imread

import threading

elbow_model = None
finger_model = None
forearm_model = None
hand_model = None
humerus_model = None
shoulder_model = None
wrist_model = None
bone_model = None

def load_frac_model(weights_path):
    st = time.time()
    with open('models/model.json', 'r') as model_data:
        loaded_model_json = model_data.read()
        model = keras.models.model_from_json(loaded_model_json)
        model.load_weights(weights_path)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (' + weights_path + ")")
        return model

def load_bone_model():
    st = time.time()        
    with open('models/bone_model.json', 'r') as model_data:
        loaded_model_json = model_data.read()
        global bone_model
        bone_model = keras.models.model_from_json(loaded_model_json)
        bone_model.load_weights('models/bone_weights.keras')
        bone_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        print(f'Time elapsed = {time.time() - st} sec (Bone Model)')

def load_wrist_model():
    global wrist_model
    wrist_model = load_frac_model('models/wrist_86.65_weights.keras')

def load_hand_model():
    global hand_model
    hand_model = load_frac_model('models/hand_79.96_weights.keras')

def load_forearm_model():
    global forearm_model
    forearm_model = load_frac_model('models/forearm_80.07_weights.keras')

def load_shoulder_model():
    global shoulder_model
    shoulder_model = load_frac_model('models/shoulder_81.53_weights.keras')

def load_elbow_model():
    global elbow_model
    elbow_model = load_frac_model('models/elbow_86.67_weights.keras')

def load_finger_model():
    global finger_model 
    finger_model = load_frac_model('models/finger_80.04_weights.keras')

def load_humerus_model():
    global humerus_model 
    humerus_model = load_frac_model('models/humerus_88.89_weights.keras')


# Load all model architectures
threading.Thread(target=load_bone_model).start()
threading.Thread(target=load_wrist_model).start()
threading.Thread(target=load_hand_model).start()
threading.Thread(target=load_forearm_model).start()
threading.Thread(target=load_shoulder_model).start()
threading.Thread(target=load_elbow_model).start()
threading.Thread(target=load_finger_model).start()
threading.Thread(target=load_humerus_model).start()

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
    bone_type = np.array(predict_bone(image_path))
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
