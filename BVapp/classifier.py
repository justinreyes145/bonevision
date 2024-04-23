import tensorflow as tf
from tensorflow import keras
import numpy as np
from skimage import transform
from skimage.io import imread


img_width, img_height = 224, 224

# Load all models
elbow_model = keras.models.load_model('models/dense169_elbow_74_62_acc.keras', compile=False)
elbow_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

finger_model = keras.models.load_model('models/dense169_finger_70_07_acc.keras', compile=False)
finger_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

forearm_model = keras.models.load_model('models/dense169_forearm_75_75_acc.keras', compile=False)
forearm_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

hand_model = keras.models.load_model('models/dense169_hand_62_82_acc.keras', compile=False)
hand_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

humerus_model = keras.models.load_model('models/dense169_humerus_83_33_acc.keras', compile=False)
humerus_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

shoulder_model = keras.models.load_model('models/dense169_shoulder_70_69_acc.keras', compile=False)
shoulder_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

wrist_model = keras.models.load_model('models/dense169_wrist_75_42_acc.keras', compile=False)
wrist_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

bone_model = keras.models.load_model('models/dense169_bone_identifier_90_65_acc.keras', compile=False)
bone_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


def load_image(image_path):
    np_image = imread(image_path)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (224, 224, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


def predict_elbow(image_path):
    image = load_image(image_path)
    return elbow_model.predict(image)


def predict_finger(image_path):
    image = load_image(image_path)
    return elbow_model.predict(image)


def predict_forearm(image_path):
    image = load_image(image_path)
    return elbow_model.predict(image)


def predict_hand(image_path):
    image = load_image(image_path)
    return elbow_model.predict(image)


def predict_humerus(image_path):
    image = load_image(image_path)
    return elbow_model.predict(image)


def predict_shoulder(image_path):
    image = load_image(image_path)
    return elbow_model.predict(image)


def predict_wrist(image_path):
    image = load_image(image_path)
    return elbow_model.predict(image)


def predict_bone(image_path):
    image = load_image(image_path)
    return bone_model.predict(image)


def predict_image(image_path):
    bone_type = np.array(predict_bone(image_path))
    max_index = np.argmax(bone_type)
    print(bone_type)
    print(max_index)
    fracture_prediction = None

    match max_index:
        case 0:
            fracture_prediction = predict_elbow(image_path)
        case 1:
            fracture_prediction = predict_finger(image_path)
        case 2:
            fracture_prediction = predict_forearm(image_path)
        case 3:
            fracture_prediction = predict_hand(image_path)
        case 4:
            fracture_prediction = predict_humerus(image_path)
        case 5:
            fracture_prediction = predict_shoulder(image_path)
        case 6:
            fracture_prediction = predict_wrist(image_path)
        case 7:
            return None

    print(fracture_prediction)
